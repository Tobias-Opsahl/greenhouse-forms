import streamlit as st
from streamlit_extras.stylable_container import stylable_container

from src.ctf import render_ctf_tasks
from src.quiz import render_quiz, reset_quiz_session
from src.ui.css_settings import CONTAINER_CSS, GLOBAL_CSS


def _initialize_app():
    """
    Initialize session state variables used for all the pages.
    """
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "welcome"
    if "best_quiz_score" not in st.session_state:
        st.session_state["best_quiz_score"] = 0
    if "best_ctf_score" not in st.session_state:
        st.session_state["best_ctf_score"] = 0


def render_welcome_page():
    """
    Render the welcome page.
    """
    st.header("Welcome to Greenhouse at dagen@ifi 2025!")

    col1, col2 = st.columns([1, 1])

    with col1:
        clicked_quiz = st.button("Start quiz")
        if clicked_quiz is True:
            st.session_state["current_page"] = "quiz"
            st.rerun()

    with col2:
        clicked_ctf = st.button("CTF")
        if clicked_ctf is True:
            st.session_state["current_page"] = "ctf"
            st.rerun()


def main():
    """
    Checks the applicationa and loads the corresponding page.
    """
    current_page = st.session_state["current_page"]

    if current_page == "welcome":
        render_welcome_page()
    elif current_page == "quiz":
        render_quiz()
    elif current_page == "ctf":
        render_ctf_tasks()


def display_header():
    """
    Display the header of the application, which is always present. The `Return to start` button is only
    present when one is not at the welcome page.
    """
    col1, col2, col3 = st.columns([1, 1, 1])

    if st.session_state["current_page"] != "welcome":
        with col1:
            return_clicked = st.button("Return to start")

        if return_clicked is True:
            if st.session_state["current_page"] == "quiz":
                reset_quiz_session()
            st.session_state["current_page"] = "welcome"
            st.rerun()

    with col2:
        st.write(f"Best quiz score: {st.session_state.best_quiz_score}")

    with col3:
        st.write(f"Best CTF score: {st.session_state.best_ctf_score}")


if __name__ == "__main__":
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
    _initialize_app()
    display_header()

    with stylable_container(key="about_tab", css_styles=CONTAINER_CSS):
        main()
