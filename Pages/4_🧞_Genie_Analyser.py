import streamlit as st
from PyPDF2 import PdfReader
from PyPDF2.errors import PdfReadError
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
import io
import asyncio
import threading

from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

def get_pdf_text(pdf_files):
    pdf_reader = PdfReader(pdf_files)
    text = ""
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text


def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_conversational_chain(question, context_pdf):
    context = ""
    n = 0
    for pdf in context_pdf:
            n+=1
            text = get_pdf_text(pdf)
            st.text("Running user_input function...")
            context += "This is {n}th file" 
            context += text

    
    prompt_template = """
    There are {n} Contexts provided. Try to have it all and
    Answer the question as detailed as possible from the provided context.If the answer is not in
    the provided context, just say, "answer is not available in the context". Do not provide the wrong answer.
    The Only Exception is When the Question asks about any creative Writing(
    You can answer the QUestion if the Question is Asking to Create Something Using Creativity and the answer is not in the context.
    )

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    # Configure API key
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    # Create the model
    model = genai.GenerativeModel(model_name="gemini-pro")

    # Format the prompt with the actual context and question
    prompt = prompt_template.format(n=n,context=context, question=question)
    
    # Generate content using the model
    response = model.generate_content([prompt])

    return response.text

def user_input(user_question,context):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)
    chain = get_conversational_chain(user_question,context)
    st.write(chain)
    

def run_user_input(user_question):
    st.write("Starting thread for user_input function...")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    output = loop.run_until_complete(user_input(user_question))
    st.write("User input function executed in the thread.")
    return output


if st.session_state["Login"] == "":
    st.error("Please Login to Continue")
else:
    load_dotenv()
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    st.header("Chat with PDF")    

    st.title("PDF Text Extractor")
    
    
    with st.sidebar:
    # File uploader widget
        pdf_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)
    
    # Check if a file has been uploaded
        context = ""
        if pdf_files :
        
        # Extract text from the PDF
            for pdf in pdf_files:
                text = get_pdf_text(pdf)
                context += text
        
        # Display the extracted text
                if context:
                    st.success("Text Extracted Successfully")
                else:
                    st.error("Text Cannot Be Extracted")
    

    user_question = st.text_input("Ask a Question from PDF")

    if user_question:
        user_input(user_question,pdf_files)
        


