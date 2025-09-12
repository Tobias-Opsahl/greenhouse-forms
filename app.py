import random

import streamlit as st
from streamlit_extras.stylable_container import stylable_container

from src.questions import QUESTIONS
from src.ui.css_settings import GLOBAL_CSS, CONTAINER_CSS


@st.cache_resource(show_spinner=False, ttl=360)
def shuffle_options(options):
    return random.sample(options, k=len(options))


def main():
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

    if "page" not in st.session_state:
        st.session_state.page = 0
    if "score" not in st.session_state:
        st.session_state.score = 0
    if f"submitted_{st.session_state.page}" not in st.session_state:
        st.session_state[f"submitted_{st.session_state.page}"] = False

    if st.session_state.page >= len(QUESTIONS):
        st.write(f"Done! Final score: {st.session_state.score}/{len(QUESTIONS)}")
        st.stop()

    current_question = QUESTIONS[st.session_state.page]
    submitted_flag = f"submitted_{st.session_state.page}"

    options = list(current_question["options"].keys())
    options = shuffle_options(options=options)
    options_and_answers = current_question["options"]

    st.markdown(f"<p style='font-size:18px; font-weight:500;'>{current_question['text']}</p>", unsafe_allow_html=True)
    if current_question["type"] == "single":
        answer = st.radio(
            "Choose one",
            options,
            index=None,
            key=f"answer_{st.session_state.page}",
            disabled=st.session_state[submitted_flag],
        )
    else:
        for option in options_and_answers.keys():
            st.checkbox(
                option,
                key=f"chk_{st.session_state.page}_{option}",
                disabled=st.session_state[submitted_flag],
            )

    col1, _, col2, _ = st.columns([1, 1, 1, 1])
    with col1:
        submitted = st.button("Submit", disabled=st.session_state[submitted_flag])

    feedback = st.session_state.get("feedback")
    if feedback is not None:
        col1, _ = st.columns([3, 1])
        with col1:
            if feedback is True:
                st.success("Correct :)")
            else:
                st.error("Wrong :/")
        st.session_state["feedback"] = None

    if submitted:
        st.session_state[submitted_flag] = True  # Set lock
        # Evaluate answers
        if current_question["type"] == "single":
            answer = st.session_state.get(f"answer_{st.session_state.page}")
            if current_question["options"][answer]:
                st.session_state["score"] += 1
                st.session_state["feedback"] = True
            else:
                st.session_state["feedback"] = False
        else:
            answers = [option for option in options if st.session_state[f"chk_{st.session_state.page}_{option}"]]
            correct = all(
                (options_and_answers[o] and o in answers) or (not options_and_answers[o] and o not in answers)
                for o in options
            )
            if correct:
                st.session_state["score"] += 1
                st.session_state["feedback"] = True
            else:
                st.session_state["feedback"] = False

        st.write(f"{st.session_state['feedback']=}")
        st.rerun()

    with col2:
        next_question_true = st.button("Next question", disabled=not st.session_state[submitted_flag])
    if next_question_true:
        st.session_state.page += 1
        st.rerun()


if __name__ == "__main__":
    with stylable_container(key="about_tab", css_styles=CONTAINER_CSS):
        main()
