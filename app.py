import streamlit as st

from src.ui.css_settings import GLOBAL_CSS
from src.questions import QUESTIONS
import random


def main():
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
    if "page" not in st.session_state:
        st.session_state.page = 0
    if "score" not in st.session_state:
        st.session_state.score = 0

    if st.session_state.page >= len(QUESTIONS):
        st.write(f"Done! Final score: {st.session_state.score}/{len(QUESTIONS)}")
        st.stop()

    # Current question
    current_question = QUESTIONS[st.session_state.page]
    st.write(current_question["text"])

    options = random.shuffle(list(current_question["options"].keys()))

    if current_question["type"] == "single":
        answer = st.radio("Choose one", options)
    else:
        answer = st.multiselect("Choose all that apply", current_question["options"])

    if st.button("Submit"):
        if current_question["type"] == "single":
            pass


if __name__ == "__main__":
    main()
