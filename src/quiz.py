import random

import streamlit as st

from src.questions import QUESTIONS


@st.cache_resource(show_spinner=False, ttl=360)
def shuffle_options(options):
    """
    Shuffles the options and caches the function, so that the shuffle will remain the same
    accross Streamlits many automatic reruns.

    Args:
        options (list): List of options.

    Returns:
        list: Shuffled list of options.
    """
    return random.sample(options, k=len(options))


def _initialize_quiz():
    """
    Initializes session state variables for the quiz.
    """
    if "page" not in st.session_state:
        st.session_state["page"] = 0
    if "score" not in st.session_state:
        st.session_state["score"] = 0
    if f"submitted_{st.session_state.page}" not in st.session_state:
        st.session_state[f"submitted_{st.session_state.page}"] = False


def reset_quiz_session():
    """
    Resets the state of the quiz. Sets the scores and page number to 0 and removes answers and submitted flags.
    """
    st.session_state["page"] = 0
    st.session_state["score"] = 0

    # Clear session states corresponding to questions and answers
    for i in range(len(QUESTIONS) + 1):
        st.session_state.pop(f"submitted_{i}", None)
        st.session_state.pop(f"answer_{i}", None)

    st.session_state.pop("feedback", None)


def _show_ending_screen():
    """
    Shows the ending screen of the quiz. Displays score and buttons for attempting again or returning to main screen.
    """
    if st.session_state["score"] >= st.session_state["best_quiz_score"]:
        st.session_state["best_quiz_score"] = st.session_state["score"]

    st.write(f"Done! Final score: {st.session_state.score}/{len(QUESTIONS)}")

    col1, col2 = st.columns([1, 1])
    with col1:
        try_quiz_again = st.button("Try quiz again")

    with col2:
        return_to_start = st.button("Return to start")

    if try_quiz_again is True:
        reset_quiz_session()
        st.rerun()

    if return_to_start is True:
        reset_quiz_session()
        st.session_state["current_page"] = "welcome"
        st.rerun()


def _render_question(current_question, submitted_flag):
    """
    Renders a questions. Shows the question text on screen, then the appropriate options given if the answer has
    a single or multiple correct answers. Collect the answers and returns the indexes corresponding to the answered
    options in a list.

    Args:
        current_question (dict): Data structur of the questions, from `src.questions.py`.
        submitted_flag (str): String representing if the current question has been submitted or not.

    Returns:
        list of int: List of the answered indexes. May be empty.
    """
    # Display question text in medium boldness
    st.markdown(f"<p style='font-size:18px; font-weight:500;'>{current_question['text']}</p>", unsafe_allow_html=True)

    # Maps options to indexes, sort of the other way around than the questions datastructure.
    options_dict = {value["option"]: index for index, value in current_question["options"].items()}

    shuffled_options = shuffle_options(list(options_dict.keys()))
    answer_indexes = []

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
            answer_indexes.append(options_dict[choice])
        return answer_indexes

    # Multiple correct answers
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
    """
    Displays feedback with Streamlit, depending on the value of "feedback" in the session state.
    """
    feedback = st.session_state.get("feedback")
    if feedback is not None:
        col1, _ = st.columns([3, 1])
        with col1:
            if feedback is True:
                st.success("Correct :)")
            else:
                st.error("Wrong :/")
        st.session_state["feedback"] = None


def _process_answer(answer_indexes, current_question):
    """
    Given an answer and a question, finds out if the answer was correct or not.

    Args:
        answer_indexes (list of int): List of the indexes corresponding to the answered options. May be empty.
        current_question (dict): Data structure of the question, from `questions.py`.
    """
    # Single correct answer_indexes
    if current_question["type"] == "single":
        if answer_indexes == []:
            st.session_state["feedback"] = False
            st.rerun()
            return
        answer_index = answer_indexes[0]
        correct = current_question["options"][answer_index]["validity"]
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
            if index not in answer_indexes:
                correct = False
        if value["validity"] is False:
            if index in answer_indexes:
                correct = False
    if correct is True:
        st.session_state["score"] += 1
        st.session_state["feedback"] = True
    else:
        st.session_state["feedback"] = False

    st.rerun()


def render_quiz():
    """
    Renders the full quiz. Calls help functions and updates session states.
    """
    _initialize_quiz()

    if st.session_state.page >= len(QUESTIONS):
        _show_ending_screen()
        return

    current_question = QUESTIONS[st.session_state.page]
    submitted_flag = f"submitted_{st.session_state.page}"

    answer_indexes = _render_question(current_question=current_question, submitted_flag=submitted_flag)

    col1, col2 = st.columns([1, 1])
    with col1:
        submitted = st.button("Submit", disabled=st.session_state[submitted_flag])

    _show_feedback()

    if submitted:
        st.session_state[submitted_flag] = True  # Set lock
        _process_answer(answer_indexes=answer_indexes, current_question=current_question)

    with col2:
        next_question_true = st.button("Next question", disabled=not st.session_state[submitted_flag])
    if next_question_true is True:
        st.session_state.page += 1
        st.rerun()
