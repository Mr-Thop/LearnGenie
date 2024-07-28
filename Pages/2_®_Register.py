import streamlit as st
from passlib.hash import sha256_crypt
import mysql.connector as sql

# Function for user registration
def register():
    # Connection parameters
    db_host = 'sportan-sportans.g.aivencloud.com'
    db_port = 10931
    db_user = 'avnadmin'
    db_password = 'AVNS_rQv-tHW54YDLIuObu2M' #Replace with your actual password
    db_name = 'defaultdb'

    try:
        # Establish a connection
        connection = sql.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            passwd=db_password,
            db=db_name
        )
        cursor = connection.cursor()
    except sql.Error as e:
        print(f"Error: {e}")
    st.subheader("Register")
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    role = st.selectbox("Role", ("Student", "Teacher"))

    if st.button("Register"):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM LGusers WHERE email = %s", (email,))
        user = cursor.fetchone()

        if user:
            st.error("User already exists. Please log in.")
        else:
            hashed_password = sha256_crypt.hash(password)
            cursor.execute("INSERT INTO LGusers (name, email, password, role) VALUES (%s, %s, %s, %s)", (name, email, hashed_password, role))
            connection.commit()
            cursor.close()
            st.success("Registration successful. You can now log in.")

# Function for user login
def login():
    # Connection parameters
    db_host = 'sportan-sportans.g.aivencloud.com'
    db_port = 10931
    db_user = 'avnadmin'
    db_password = 'AVNS_rQv-tHW54YDLIuObu2M' #Replace with your actual password
    db_name = 'defaultdb'

    try:
        # Establish a connection
        connection = sql.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            passwd=db_password,
            db=db_name
        )
        cursor = connection.cursor()
    except sql.Error as e:
        print(f"Error: {e}")
    st.subheader("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        cursor.execute("SELECT * FROM LGusers WHERE email = %s", (email,))
        user = cursor.fetchone()

        if user:
            hashed_password = user[3]  # Assuming 'password' is the fourth column
            if sha256_crypt.verify(password, hashed_password):
                st.success("Login successful")
                st.write(f"Welcome to LearnGenie , Mr/Mrs {user[1]}  !")
                st.write(f"Your {user[4]} Id is {user[0]}")
                
                return user # Return the user record
            else:
                st.error("Invalid login. Please check your credentials.")
        else:
            st.error("User not found. Please register first.")
    return None



with st.sidebar:
    selected_option=st.radio("Select an Option",["Register","Login"])

if selected_option=="Register":
    register()
else:
    user=login()
    if user:
        st.session_state["Login"]=user[4]
        st.session_state["Id"]=user[0]
        st.session_state["Name"]=user[1]
    
