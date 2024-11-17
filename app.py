import streamlit as st
import pickle
from main_page import main_page
from technical_details import technical_details
import time


#This sets basic page configs.
st.set_page_config(
    page_title="Mushroom Edibility Classifier",
    page_icon="🍄‍🟫",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    /* Sidebar background color */
    [data-testid="stSidebar"] {
        background-color: #CEA876;
    }

    /* Sidebar text color */
    [data-testid="stSidebar"]  {
        color: #CEA876;
    }

    /* Sidebar toggle button */
    .sidebar-toggle-btn {
        background-color: #CEA876; /* Color of the button */
        color: black;
        border: none;
        padding: 8px;
        border-radius: 4px;
        cursor: pointer;
        margin: 10px;
    }

        .stButton button {
        background-color: #613b26; /* Button background color */
        color: white; /* Button text color */
        border: none;
        border-radius: 4px;
        padding: 8px 16px;
    }
    .stButton button:hover {
        background-color: #D9A45C; /* Button color on hover */
        color: white; /* Text color on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)


#This function calls the different pages depending on the sidebar selection.
def main():
    st.sidebar.title("🌳 Chapters of the Forest 🌳")

    # Initialize session state for page selection
    if "page" not in st.session_state:
        st.session_state.page = "Main Page"

    # Buttons to navigate pages
    if st.sidebar.button("Main Page", use_container_width=True):
        st.session_state.page = "Main Page"
    if st.sidebar.button("Technical Details", use_container_width=True):
        st.session_state.page = "Technical Details"

    # Render the selected page
    if st.session_state.page == "Main Page":
        main_page()
    elif st.session_state.page == "Technical Details":
        technical_details()
if __name__ == "__main__":
    main()