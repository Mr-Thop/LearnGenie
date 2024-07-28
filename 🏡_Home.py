import streamlit as st

st.set_page_config(page_title="LearnGenie || EdTech || Personalized Learning Paths", layout="wide")
st.sidebar.write("Created with  ❤  by Team R^4")

# --- Page Setup ---

home_page = st.Page(
    page="./Pages/Home.py",
    title="🏡 Home",
    default= True
)
about_page = st.Page(
     page = "./Pages/1_💙_About_Us.py",
     title = "About Us" 
     )

login_page = st.Page(
     page = "./Pages/2_®_Register.py",
     title = "Register"
     )

test_page = st.Page(
     page= "./Pages/3_📜_Analysis_Test.py",
     title ="Analysis Test"
     )

analyse_page = st.Page(
     page= "./Pages/4_🧞_Genie_Analyser.py",
     title="Genie Analyser"
)

bot_page = st.Page(
     page="./Pages/5_🤖_Genie_Bot.py",
     title="Genie Bot"
)

# --- Navigation ---

pg = st.navigation(pages=[home_page,about_page,login_page,test_page,analyse_page,bot_page])

pg.run()

