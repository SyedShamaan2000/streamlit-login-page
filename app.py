import streamlit as st
from dashboard import dashboard
from signin import signin

# Initialize session state
def initialize():
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "signin"
    if "is_authenticated" not in st.session_state:
        st.session_state["is_authenticated"] = False
    if "user_id" not in st.session_state:
        st.session_state["user_id"] = None
    if "access_token" not in st.session_state:
        st.session_state["access_token"] = None

def main():
    initialize()
    st.write("This is in session from current page: ",st.session_state["current_page"])
    st.write("This is in session from is auth: ",st.session_state["is_authenticated"])
    st.write("This is in session from user ID: ",st.session_state["user_id"])
    st.write("This is in session from access token: ",st.session_state["access_token"])
    
    if not st.session_state["is_authenticated"]:
        st.write("Not Authenticated")
        st.session_state["current_page"] = "signin"
        st.write("Its Signin Page", st.session_state["current_page"])
        signin()
    else:
        st.write("Authenticated")
        st.session_state["current_page"] = "dashboard"
        st.write("Its Dashboard Page", st.session_state["current_page"])
        dashboard()



main()