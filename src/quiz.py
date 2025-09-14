import random

import streamlit as st

from src.questions import QUESTIONS


@st.cache_resource(show_spinner=False, ttl=360)
def shuffle_options(options):
    return random.sample(options, k=len(options))


def _initialize_quiz():
    if "page" not in st.session_state:
        st.session_state["page"] = 0
    if "score" not in st.session_state:
        st.session_state["score"] = 0
    if f"submitted_{st.session_state.page}" not in st.session_state:
        st.session_state[f"submitted_{st.session_state.page}"] = False


def _reset_quiz_session():
    st.session_state["page"] = 0
    st.session_state["score"] = 0
    for i in range(len(QUESTIONS) + 1):
        if f"submitted_{i}" in st.session_state:
            st.session_state[i] = False
        if f"answer_{i}" in st.session_state:
            st.session_state[i] = False


def _show_ending_screen():
    st.write(f"Done! Final score: {st.session_state.score}/{len(QUESTIONS)}")

    col1, col2 = st.columns([1, 1])
    with col1:
        try_quiz_again = st.button("Try quiz again")

    with col2:
        return_to_start = st.button("Return to start")

    if try_quiz_again is True:
        _reset_quiz_session()
        st.rerun()

    if return_to_start is True:
        st.session_state["current_page"] = "welcome"
        st.rerun()


def _render_question(current_question, options, options_and_answers, submitted_flag):
    st.markdown(f"<p style='font-size:18px; font-weight:500;'>{current_question['text']}</p>", unsafe_allow_html=True)
    if current_question["type"] == "single":
        st.radio(
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


def _show_feedback():
    feedback = st.session_state.get("feedback")
    if feedback is not None:
        col1, _ = st.columns([3, 1])
        with col1:
            if feedback is True:
                st.success("Correct :)")
            else:
                st.error("Wrong :/")
        st.session_state["feedback"] = None


def _process_answer(answer, current_question, options, options_and_answers, submitted_flag):
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


def render_quiz():
    _initialize_quiz()
    st.write(f"{list(st.session_state.keys())=}")

    if st.session_state.page >= len(QUESTIONS):
        _show_ending_screen()
        return

    current_question = QUESTIONS[st.session_state.page]
    submitted_flag = f"submitted_{st.session_state.page}"
    options = list(current_question["options"].keys())
    options = shuffle_options(options=options)
    options_and_answers = current_question["options"]
    answer = _render_question(
        current_question=current_question,
        options=options,
        options_and_answers=options_and_answers,
        submitted_flag=submitted_flag,
    )

    col1, _, col2, _ = st.columns([1, 1, 1, 1])
    with col1:
        submitted = st.button("Submit", disabled=st.session_state[submitted_flag])

    _show_feedback()

    if submitted:
        _process_answer(
            answer=answer,
            current_question=current_question,
            options=options,
            options_and_answers=options_and_answers,
            submitted_flag=submitted_flag,
        )

    with col2:
        next_question_true = st.button("Next question", disabled=not st.session_state[submitted_flag])
    if next_question_true is True:
        st.session_state.page += 1
        st.rerun()
