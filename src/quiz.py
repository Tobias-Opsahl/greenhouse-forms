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

    # Clear session states corresponding to questions and answers
    for i in range(len(QUESTIONS) + 1):
        st.session_state.pop(f"submitted_{i}", None)
        st.session_state.pop(f"answer_{i}", None)
        st.session_state.pop(f"submitted_{i}", None)

    st.session_state.pop("feedback", None)


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
        _reset_quiz_session()
        st.session_state["current_page"] = "welcome"
        st.rerun()


def _render_question(current_question, submitted_flag):
    st.markdown(f"<p style='font-size:18px; font-weight:500;'>{current_question['text']}</p>", unsafe_allow_html=True)
    options_dict = {value["option"]: index for index, value in current_question["options"].items()}
    shuffled_options = shuffle_options(list(options_dict.keys()))

    # Single correct answer
    if current_question["type"] == "single":
        choice = st.radio(
            "Choose one",
            shuffled_options,
            index=None,
            key=f"answer_{st.session_state.page}",
            disabled=st.session_state[submitted_flag],
        )
        if choice is not None:
            answer_index = options_dict[choice]
            return answer_index
        return None

    # Multiple correct answers
    answer_indexes = []
    for option in shuffled_options:
        index = options_dict[option]
        checked = st.checkbox(
            option,
            key=f"chk_{st.session_state.page}_{option}",
            disabled=st.session_state[submitted_flag],
        )
        if checked is True:
            answer_indexes.append(index)
    return answer_indexes


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


def _process_answer(answer, current_question, submitted_flag):
    st.session_state[submitted_flag] = True  # Set lock

    # Single correct answer
    if current_question["type"] == "single":
        if answer is None:
            st.session_state["feedback"] = False
            st.rerun()
            return
        correct = current_question["options"][answer]["validity"]
        if correct is True:
            st.session_state["score"] += 1
            st.session_state["feedback"] = True
        else:
            st.session_state["feedback"] = False
        st.rerun()
        return

    # Multiple correct answers
    correct = True
    for index, value in current_question["options"].items():
        if value["validity"] is True:
            if index not in answer:
                correct = False
        if value["validity"] is False:
            if index in answer:
                correct = False
    if correct is True:
        st.session_state["score"] += 1
        st.session_state["feedback"] = True
    else:
        st.session_state["feedback"] = False

    st.rerun()


def render_quiz():
    _initialize_quiz()

    if st.session_state.page >= len(QUESTIONS):
        _show_ending_screen()
        return

    current_question = QUESTIONS[st.session_state.page]
    submitted_flag = f"submitted_{st.session_state.page}"

    answer = _render_question(current_question=current_question, submitted_flag=submitted_flag)

    col1, _, col2, _ = st.columns([1, 1, 1, 1])
    with col1:
        submitted = st.button("Submit", disabled=st.session_state[submitted_flag])

    _show_feedback()

    if submitted:
        _process_answer(answer=answer, current_question=current_question, submitted_flag=submitted_flag)

    with col2:
        next_question_true = st.button("Next question", disabled=not st.session_state[submitted_flag])
    if next_question_true is True:
        st.session_state.page += 1
        st.rerun()
