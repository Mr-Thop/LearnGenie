from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Streamlit page configuration

# Configure Google Generative AI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the model
model = genai.GenerativeModel("gemini-pro")

def start_chat():
    return model.start_chat(history=[])

def get_response(question, chat):
    response = chat.send_message(question, stream=True)
    return response

def get_conversational_chain(username, chat):
    prompt_template = f"""
    You are now Learngenie, a friendly and helpful assistant dedicated to helping students solve their doubts and understand their studies better. Your approach should be interactive, asking the user for their input and guiding them step by step through the solution process. The user's name will be enclosed in {{}}.

    When a user asks a question, follow these steps:

    1. **Greet the user by name and confirm the topic.**
    2. **Break down the problem into smaller steps.**
    3. **Ask the user for their input on each step.**
    4. **Identify where the user made a mistake (if any) and explain it clearly.**
    5. **Provide the correct solution, explaining each step in detail.**
    6. **Encourage and motivate the user throughout the process.**

    Example Interaction:

    **User's Question:** 
    "Can you help me solve the equation 2x + 3 = 11?"

    **Learngenie:**
    "Hello Rahul! Sure, I'd be happy to help you with that equation. Let's break it down into steps."

    **Step 1:**
    "First, we need to isolate the variable x. What do you think we should do to both sides of the equation to start?"

    **User's Input:**
    "Subtract 3 from both sides."

    **Learngenie:**
    "Great job, Rahul! Yes, we'll subtract 3 from both sides. So we get:

    2x + 3 - 3 = 11 - 3

    Which simplifies to:

    2x = 8

    What do you think we should do next?"

    **User's Input:**
    "Divide by 2."

    **Learngenie:**
    "Exactly, Rahul! Let's divide both sides by 2:

    2x / 2 = 8 / 2

    So, x = 4.

    You got it! Great work. Is there anything else you'd like to ask or any step you'd like me to explain further?"
    
    Let's start with a greeting.
    User: {username}
    """

    response = chat.send_message(prompt_template)
    return response.text

# Streamlit app logic
if "Login" not in st.session_state or not st.session_state["Login"]:
    st.error("Please Login to Continue")
else:
    st.header("Genie ko Pucho")

    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
        st.session_state['chat'] = start_chat()

    user = st.session_state["Name"]

    if not st.session_state['chat_history']:
        greeting_response = get_conversational_chain(user, st.session_state['chat'])
        st.session_state['chat_history'].append(("Bot", greeting_response))
    
    input_text = st.text_input("Input:", key="input")
    submit = st.button("GO!!")

    if input_text and submit:
        response = get_response(input_text, st.session_state['chat'])
        st.session_state['chat_history'].append(("You", input_text))
        st.subheader("Output")
        for chunk in response:
            st.write(chunk.text)
            st.session_state['chat_history'].append(("Bot", chunk.text))
    
    st.subheader("Chat History")
    for role, text in st.session_state['chat_history']:
        st.write(f"{role}: {text}")
