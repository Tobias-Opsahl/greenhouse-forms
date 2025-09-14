import streamlit as st
from src.ctf_tasks import CTF_TASKS, CTF_ABOUT


def _initialize_ctf():
    """
    Initialize session state for CTF tasks.
    """
    if st.session_state.get("ctf_tasks_completed") is None:
        st.session_state["ctf_tasks_completed"] = {i: False for i in range(len(CTF_TASKS) + 2)}
    if st.session_state.get("ctf_score") is None:
        st.session_state["ctf_score"] = 0
    if st.session_state.get("ctf_task_active_index") is None:
        st.session_state["ctf_task_active_index"] = None


def _display_about():
    """
    Display the header and about information.
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
    user_answer = user_answer.lower().strip().strip("<").strip(">")
    for task_answer in task_answers:
        task_answer = task_answer.lower().strip()
        if user_answer == task_answer:
            return True

    return False


def reset_ctf_session():
    """
    Resets the session variable for the current session.
    """
    st.session_state["ctf_task_active_index"] = None


def _display_ctf_task():
    """
    Display a single CTF OSINT task and check the answer.
    """
    task_index = st.session_state.get("ctf_task_active_index")
    task = CTF_TASKS[task_index]

    st.header(task["title"])
    st.write(task["text"])

    user_answer = st.text_input(f"Answer: {task['answer_text']}", key="ctf_user_text_input")
    correct = _check_answer(user_answer=user_answer, task_answers=task["answer"])

    if task["hint"] is not None:
        with st.expander("Show hint:", expanded=False):
            st.write(task["hint"])

    col1, col2 = st.columns([1, 1])

    with col1:
        submit_clicked = st.button("Submit", key="submit_from_osint_ctf")

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
        return_clicked = st.button("Return to CTF", key="return_to_ctf")

    if return_clicked is True:
        reset_ctf_session()
        st.rerun()


def _render_web_task1():
    if "ctf_init" not in st.session_state:
        val = st.query_params.get("enable_button", "false")
        if isinstance(val, list):
            val = val[0]
        if str(val).lower() != "true":
            st.query_params.update({"enable_button": "false"})
        st.session_state["ctf_init"] = True
        st.session_state["ctf_unlocked"] = False

    # Read current param and decide enabled/disabled
    qp_val = st.query_params.get("enable_button", "false")
    if isinstance(qp_val, list):
        qp_val = qp_val[0]
    enabled = str(qp_val).lower() == "true"

    col1, col2 = st.columns([1, 1])

    with col1:
        clicked = st.button("Get flag", disabled=not enabled, key="get_flag_button")
    if clicked:
        if st.session_state["ctf_tasks_completed"][st.session_state["ctf_task_active_index"]] is False:
            st.session_state["ctf_tasks_completed"][st.session_state["ctf_task_active_index"]] = True
            st.session_state["ctf_score"] += 1

        if st.session_state["ctf_score"] >= st.session_state["best_ctf_score"]:
            st.session_state["best_ctf_score"] = st.session_state["ctf_score"]

        st.success(f"Correct! CTF Score: {st.session_state['ctf_score']}")

    with col2:
        return_clicked = st.button("Return to CTF", key="return_to_ctf_from_web1")

    if return_clicked is True:
        reset_ctf_session()
        st.rerun()


def _render_web_task2():
    question = "Who is the only winner of a Turing award and a Nobel prize in physics?"
    options = [
        "Albert Einstein",
        "Claude Shannon",
        "Ada Lovelace",
        "Yann LeCun",
        "Richard Sutton",
        "Grace Hopper",
        "Donald Knuth",
    ]
    correct = "Hinton"

    # One-time init: set default only if no URL param present (store last name)
    if "ctf2_init" not in st.session_state:
        val = st.query_params.get("answer")
        if isinstance(val, list):
            val = val[0]
        if not val:
            st.query_params.update({"answer": options[0].rsplit(" ", 1)[-1]})
        st.session_state["ctf2_init"] = True

    # Read param (last name) and find matching option by substring (case-insensitive)
    qp_answer = st.query_params.get("answer", options[0].rsplit(" ", 1)[-1])
    if isinstance(qp_answer, list):
        qp_answer = qp_answer[0]
    qp_answer_l = str(qp_answer).strip().lower()

    # Does the URL last name appear in any full-name option?
    match_index = next((i for i, opt in enumerate(options) if qp_answer_l and qp_answer_l in opt.lower()), 0)
    in_substring = any(qp_answer_l in opt.lower() for opt in options)

    st.write(question)
    choice = st.selectbox(
        "Choose the correct answer",
        options,
        index=match_index,
        key="ctf2_choice",
    )

    # Mirror selectbox to URL ONLY if current URL param already corresponds to an option
    selected_last = choice.rsplit(" ", 1)[-1]
    if in_substring and qp_answer_l != selected_last.lower():
        st.query_params.update({"answer": selected_last})

    col1, col2 = st.columns([1, 1])
    with col1:
        submitted = st.button("Submit answer", key="ctf2_submit")

    if submitted:
        # Re-read param; user may have set the correct answer in URL
        final = st.query_params.get("answer", "")
        if isinstance(final, list):
            final = final[0]
        if str(final).strip().lower() == correct.lower():
            if st.session_state["ctf_tasks_completed"][st.session_state["ctf_task_active_index"]] is False:
                st.session_state["ctf_tasks_completed"][st.session_state["ctf_task_active_index"]] = True
                st.session_state["ctf_score"] += 1
            if st.session_state["ctf_score"] >= st.session_state["best_ctf_score"]:
                st.session_state["best_ctf_score"] = st.session_state["ctf_score"]
            st.success(f"Correct! CTF Score: {st.session_state['ctf_score']}")
        else:
            st.error("Wrong, please try again.")

    with col2:
        return_clicked = st.button("Return to CTF", key="return_to_ctf_from_web2")
    if return_clicked:
        reset_ctf_session()
        st.rerun()


def _display_web_task():
    if st.session_state["ctf_task_active_index"] == len(CTF_TASKS):
        _render_web_task1()
    if st.session_state["ctf_task_active_index"] == len(CTF_TASKS) + 1:
        _render_web_task2()


def render_ctf_tasks():
    """
    Render the full CTF page.
    """
    _initialize_ctf()
    _display_about()

    clicked_index = None

    if st.session_state["ctf_task_active_index"] is None:
        st.markdown("<p style='font-size:18px; font-weight:500;'>OSINT:</p>", unsafe_allow_html=True)
        col1, col2 = st.columns([1, 1])

        for i, task in enumerate(CTF_TASKS):
            col = col1 if i < len(CTF_TASKS) / 2 else col2
            with col:
                clicked = st.button(task["title"])
                if clicked is True:
                    clicked_index = i

        st.markdown("<p style='font-size:18px; font-weight:500;'>WEB:</p>", unsafe_allow_html=True)

        col1, col2 = st.columns([1, 1])

        with col1:
            clicked = st.button("Web1", key="web1_button")
            if clicked is True:
                clicked_index = len(CTF_TASKS)

        with col2:
            clicked = st.button("Web2", key="web2_button")
            if clicked is True:
                clicked_index = len(CTF_TASKS) + 1

    if clicked_index is not None:
        st.session_state["ctf_task_active_index"] = clicked_index
        st.rerun()

    if st.session_state["ctf_task_active_index"] is not None:
        if st.session_state["ctf_task_active_index"] < len(CTF_TASKS):
            _display_ctf_task()
        else:
            _display_web_task()
