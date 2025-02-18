import streamlit as st
from st_bridge import bridge, html
import time
import streamlit.components.v1 as components

def get_current_user(key):
    access_token = st.session_state.get("access_token")
    if access_token:
        return access_token
    data = bridge("my-bridge", default=None, key=key)
    if not access_token:
        components.html("""
            <script>
                function sendData() {
                if (window.parent.stBridges) {
                    const data = localStorage.getItem('auth-token') 
                    window.parent.stBridges.send('my-bridge', data);
                } else {
                    console.log("stBridges is not available yet.");
                }
            }
            setTimeout(sendData, 100); // Delay execution to ensure availability
            </script>
        """)
        time.sleep(0.2)
        return data



def set_user_session(result: dict):
    # print("Running inside set_user_session")
    # print(result.get("access_token"))
    components.html(f"""
    <script>
        function setLocalStorage() {{
            // console.log("Setting Local Storage");
            localStorage.setItem('auth-token', '{result.get('access_token')}');
            // console.log("Set Local Storage: ", localStorage.getItem('auth-token'));
        }}
        setTimeout(setLocalStorage, 100)
    </script>
    """)
    time.sleep(0.2)
    # print("Set session")
    st.session_state["access_token"] = result.get('access_token')
    st.session_state["is_authenticated"] = True
    # print("set the authentication", st.session_state["is_authenticated"])
    # st.session_state["user_id"] = result.get('user_id')
    # st.session_state["user_email"] = result.get('email')
    # st.session_state['user_name'] = result.get('user_name')

def clear_user_session():
    if st.session_state["access_token"]:
        del st.session_state["access_token"]
    st.session_state["is_authenticated"] = False
    components.html(f"""
    <script>
        function removeLocalStorage() {{
            // console.log("Removing Local Storage");
            localStorage.removeItem('auth-token');
        }}
        setTimeout(removeLocalStorage, 100)
    </script>
    """)
    time.sleep(0.2)