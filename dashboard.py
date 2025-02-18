import streamlit as st
from auth_utils import get_current_user, clear_user_session
import streamlit.components.v1 as components

def dashboard():
    st.write("THIS IS COMING FROM THE FUNCTION IN THE DASHBOARD")
    # current_user = get_current_user("dashboard")
    # st.write("current user is: ", current_user)
    if st.button("Logout"):
        clear_user_session()
        components.html("<script>parent.window.location.reload()</script>")