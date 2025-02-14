import streamlit as st

def signin():
    st.write("THIS IS COMING FROM THE FUNCTION IN THE SIGNIN")
    if "signin_form" not in st.session_state:
        st.session_state.signin_form = {"email": ""}
        st.write(st.session_state.signin_form)