import streamlit as st

# Initialize task list in session state to persist across reruns
if 'tasks' not in st.session_state:
    st.session_state['tasks'] = []

# Title of the app
st.title("To-Do List App")

# Input box for a new task
new_task = st.text_input("Enter a new task:")

# Button to add a task
if st.button("Add Task"):
    if new_task:
        st.session_state['tasks'].append({"task": new_task, "done": False})
        st.success(f"Task '{new_task}' added!")

# Display the list of tasks
if st.session_state['tasks']:
    st.write("### Your Tasks:")
    for i, task in enumerate(st.session_state['tasks']):
        done = st.checkbox(f"{task['task']}", value=task['done'], key=i)
        if done:
            st.session_state['tasks'][i]['done'] = True
            st.success(f"Task '{task['task']}' marked as done!")

# Button to clear completed tasks
if st.button("Clear Completed Tasks"):
    st.session_state['tasks'] = [task for task in st.session_state['tasks'] if not task['done']]
    st.success("Completed tasks cleared!")
