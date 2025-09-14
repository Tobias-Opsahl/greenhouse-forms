import streamlit as st
from src.ctf_tasks import CTF_TASKS, CTF_ABOUT


def _initialize_ctf():
    """
    Initialize session state for CTF tasks.
    """
    if st.session_state.get("ctf_tasks_completed") is None:
        st.session_state["ctf_tasks_completed"] = {i: False for i in range(len(CTF_TASKS))}
    if st.session_state.get("ctf_score") is None:
        st.session_state["ctf_score"] = 0
    if st.session_state.get("ctf_task_active_index") is None:
        st.session_state["ctf_task_active_index"] = None


def _display_about():
    """
    Displau the header and about information.
    """
    if st.session_state.get("ctf_task_active_index") is None:
        st.header("Capture the Flag (CTF)")
        st.write(CTF_ABOUT)


def _check_answer(user_answer, task_answers):
    """
    Check if a user answer matches any of the correct answers.

    Args:
        user_answer (str): The answer from the user.
        task_answers (list of str): List of the accepted answers from the task.

    Returns:
        bool: True if the answer was currect, False if not.
    """
    user_answer = user_answer.lower().strip()
    for task_answer in task_answers:
        task_answer = task_answer.lower().strip()
        if user_answer == task_answer:
            return True

    return False


def _display_ctf_task():
    """
    Display a single CTF OSINT task and check the answer.
    """
    task_index = st.session_state.get("ctf_task_active_index")
    task = CTF_TASKS[task_index]

    st.header(task["title"])
    st.write(task["text"])

    user_answer = st.text_input(f"Answer: {task['answer_text']}")
    correct = _check_answer(user_answer=user_answer, task_answers=task["answer"])

    if task["hint"] is not None:
        with st.expander("Show hint:", expanded=False):
            st.write(task["hint"])

    col1, col2 = st.columns([1, 1])

    with col1:
        submit_clicked = st.button("Submit")

    if submit_clicked is True:
        if correct is True:
            if st.session_state["ctf_tasks_completed"][task_index] is False:
                st.session_state["ctf_tasks_completed"][task_index] = True
                st.session_state["ctf_score"] += 1

            if st.session_state["ctf_score"] >= st.session_state["best_ctf_score"]:
                st.session_state["best_ctf_score"] = st.session_state["ctf_score"]

            st.success(f"Correct! CTF Score: {st.session_state['ctf_score']}")
        else:
            st.error("Wrong, please try again")

    with col2:
        return_clicked = st.button("Return to CTF")

    if return_clicked is True:
        st.session_state["ctf_task_active_index"] = None
        st.rerun()


def render_ctf_tasks():
    """
    Render the full CTF page.
    """
    _initialize_ctf()
    _display_about()

    clicked_index = None

    if st.session_state["ctf_task_active_index"] is None:
        col1, col2 = st.columns([1, 1])

        for i, task in enumerate(CTF_TASKS):
            col = col1 if i < len(CTF_TASKS) / 2 else col2
            with col:
                clicked = st.button(task["title"])
                if clicked is True:
                    clicked_index = i

    if clicked_index is not None:
        st.session_state["ctf_task_active_index"] = clicked_index
        st.rerun()

    if st.session_state["ctf_task_active_index"] is not None:
        _display_ctf_task()
