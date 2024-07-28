import streamlit as st

st.set_page_config(page_title="About Us | Team R^4",layout="wide")

st.title("About Us")

st.sidebar.write("Created with  ❤  by Team R^4")


st.write("In our first year of studies, we embarked on a remarkable journey to create this project, a journey that served as a testament to our collective ideas and boundless creativity. This endeavor, though undoubtedly challenging, proved to be an immensely rewarding experience that has left an indelible mark on each of us.")
st.write("Throughout this journey, there were countless late nights spent debugging code and endless iterations as we sought perfection. Despite the inevitable hurdles, our unwavering passion for our work, coupled with the steadfast support of our mentor, served as the bedrock upon which we persevered and thrived.")
st.write("As we stand here today, presenting our project to the world, we are profoundly grateful for the privilege of having you visit and bear witness to the tangible result of our dedication and hard work. It is our hope that our project, the culmination of countless hours of labor and unwavering determination, proves to be not only inspiring but also informative to all those who engage with it.")

st.write("---")

st.header("Team R^4")

st.text("")
st.text("")

_,col1,_,col2,_,col3,_,col4 = st.columns([0.3,1,0.6,1,0.3,1,0.6,1])


with col1:
    st.text("")
    st.text("")
    st.image('images/reeti.jfif',width=150)
    st.text("Reeti Agarwal\nComputer Engineer")


with col3:
    st.text("")
    st.text("")
    st.image('images/karthik.jpg',width=150)
    st.text("Karthik Reddy\nAIML Engineer")

with col2:
    st.text("")
    st.text("")
    st.image('images/ria.jfif',width=150)
    st.text("Ria Vinod\nComputer Engineer")

with col4:
    st.text("")
    st.text("")
    st.image('images/ratan2.jfif',width=150)
    st.text("Ratan Maurya\nAIML Engineer")

st.write("---")
