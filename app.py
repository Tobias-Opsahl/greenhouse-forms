import streamlit as st
from streamlit_extras.stylable_container import stylable_container

from src.quiz import render_quiz
from src.ui.css_settings import GLOBAL_CSS, CONTAINER_CSS


def render_welcome_page():
    st.header("Welcome to Greenhouse's stand at dagen@ifi 2025!")

    clicked = st.button("Start quiz")
    if clicked is True:
        st.session_state["current_page"] = "quiz"
        st.rerun()


def main():
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "welcome"

    current_page = st.session_state["current_page"]

    if current_page == "welcome":
        render_welcome_page()
    elif current_page == "quiz":
        render_quiz()


if __name__ == "__main__":
    with stylable_container(key="about_tab", css_styles=CONTAINER_CSS):
        main()
