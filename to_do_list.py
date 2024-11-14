import streamlit as st 

def show_page():
    if st.session_state.page == "login_page":
        login_page()
    elif st.session_state.page == "to_do_page":
        to_do_page()

def login_page():
    st.title("Login Page")
    name = st.text_input("Enter your name")
    username = st.text_input("Enter your username")
    password = st.text_input("Enter your password", type="password")

    if st.button("Sign In"):
        # Set to-do page and initialize tasks list in session state
        st.session_state.page = "to_do_page"
        if 'tasks' not in st.session_state:
            st.session_state.tasks = []  # Initialize tasks if not already set

def to_do_page():
    st.title("TO DO LIST")
    st.header("Hi, it's great to see you!")

    # Add a new task form
    task = st.text_input("Add a new task")
    if st.button("Add Task") and task:
        st.session_state.tasks.append({"task": task, "completed": False})

    st.write("### Your Tasks")
    # Display tasks with checkboxes and change text color when completed
    for i, item in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([0.1, 5])
        with col1:
            completed = st.checkbox("", value=item["completed"], key=str(i))
        with col2:
            # Show task in green if completed, otherwise default color
            task_display = f"<span style='color: green;'>{item['task']}</span>" if completed else item["task"]
            st.markdown(task_display, unsafe_allow_html=True)
        
        # Update task completion status
        st.session_state.tasks[i]["completed"] = completed

# Initialize page state on first run
if 'page' not in st.session_state:
    st.session_state.page = "login_page"

# Show the current page based on the state
show_page()
