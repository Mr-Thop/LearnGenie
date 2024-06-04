import streamlit as st

st.set_page_config(page_title="LearnGenie || EdTech || Personalized Learning Paths", layout="wide")

st.sidebar.write("Created with  ❤  by Team R^4")
if "Login" not in st.session_state:
     st.session_state["Login"] = ""
     st.session_state["Id"] = ""
     st.session_state["Name"] = ""


# Set a title for your site
col1,col4,col2,col3=st.columns([1,0.3,5,2])
with col1:
     st.text("")
     st.image("3.jpg")

with col2:
     st.write(" ")
     st.write(" ")
     st.header("LearnGenie")

st.text("")
st.text("")

st.write("LearnGenie is an EdTech project powered by GenAI, designed to transform the learning landscape by providing a tailored, efficient, and effective educational experience for each student. It addresses the challenges posed by traditional one-size-fits-all education methods that often fail to cater to individual learning needs.The  approach is rooted in the ARCS model of motivation, ensuring that learners are fully engaged and motivated throughout their learning journey. It captures attention through interactive and dynamic content, maintains relevance by aligning learning materials with personal goals and interests, builds confidence by providing incremental challenges and positive reinforcement, and ensures satisfaction through the achievement of learning milestones and immediate feedback.")
st.write("We go beyond mere content delivery by fostering active engagement and interaction through AI-driven chatbots, personalized dashboards, and tailored content recommendations. It addresses the Two Sigma Problem, where one-on-one tutoring significantly boosts student performance, by simulating this personalized tutoring at scale. Features such as chatbots for subject-related queries, simplified concepts presented in flow charts and diagrams, and social connections make learning more interactive and enjoyable.")

st.write("---")


# Explain why the website was built
col1,_,col2=st.columns([1,0.3,1])

with col1:
     st.header("Why LearnGenie ?")
     st.text("")
     st.text("")
     st.write("LearnGenie is a groundbreaking EdTech project powered by GenAI, designed to transform the learning landscape and address the challenges of traditional one-size-fits-all education. By leveraging advanced AI and machine learning algorithms, LearnGenie tailors the learning experience to each student's unique needs, cognitive abilities, learning styles, and personal schedules. Here are five key reasons why LearnGenie stands out as an exceptional solution for personalized and effective learning : ")

     st.markdown("1. Cognitive Analysis")
     st.markdown("2. Learning Ability Assessment")
     st.markdown("3. Tailored to Learning Styles")
     st.markdown("4. Advanced AI Insight")
     st.markdown("5. Personalized Resources")

     st.write("---")
     
with col2:
     st.text("")
     st.text("")
     st.text("")
     st.text("")
     
     st.text("")
     st.text("")
     st.text("")
     st.text("")
     st.image("1.jpg",width=400)


_,col3,col1=st.columns([0.2,1,1])

with col1:
# Highlight key features
     st.header("Key Features")
     st.write("Our platform offers a range of features, including:")
     st.write("- Personalized Learning Experience")
     st.write("- AI-powered Chatbots")
     st.write("- Cognitive Performance Analysis")
     st.write("- Personalized Study Plan")
     st.write("- AI-driven Insights and Analytic")

     st.write(
    "We've also integrated a powerful AI bot to assist you with tasks, answer your questions, "
    "and provide insights. Our bot is here to make your Learning management experience even better."
     )

with col3:
     st.text("")
     st.text("")
     st.text("")
     st.image("2.jpg",width=400)