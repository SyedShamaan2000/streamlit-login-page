import streamlit as st
from dashboard import dashboard
from signin import signin
from auth_utils import get_current_user

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
    current_user = get_current_user("app")
    if current_user:
        st.session_state["is_authenticated"] = True
    else:
        st.session_state["is_authenticated"] = False
    # st.write("current user is: ", current_user)
    # st.write("This is in session from current page: ",st.session_state["current_page"])
    # st.write("This is in session from is auth: ",st.session_state["is_authenticated"])
    # st.write("This is in session from user ID: ",st.session_state["user_id"])
    # st.write("This is in session from access token: ",st.session_state["access_token"])
    
    if not st.session_state["is_authenticated"]:
        # st.write("Not Authenticated")
        # st.session_state["current_page"] = "signin"
        # st.write("Its Signin Page", st.session_state["current_page"])
        signin()
    else:
        st.session_state["current_page"] = "dashboard"
        # st.write("Authenticated")
        st.write("Its Dashboard Page", st.session_state["current_page"])
        dashboard()



main()