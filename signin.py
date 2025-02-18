import streamlit as st
from auth_utils import set_user_session

def signin():
    # st.write("THIS IS COMING FROM THE FUNCTION IN THE SIGNIN")
    if "signin_form" not in st.session_state:
        st.session_state.signin_form = {"email": ""}
    # st.write(st.session_state.signin_form)
    email = st.text_input("Email")
    password = st.text_input("Password")
    if st.button("Login"):
        if email and password:
            st.success("Login Successfull")
            try:
                set_user_session({"email": email, "password": password, "access_token": 123456, "user_name": email})
                st.rerun()
            except Exception as e:
                print("Error in loggin in", e)
        else:
            st.error("Email and Password are required")