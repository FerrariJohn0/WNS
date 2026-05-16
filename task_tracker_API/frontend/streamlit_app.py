
import streamlit as st
import requests
import pandas as pd

API_url = "http://127.0.0.1:8000/tasks"
st.title("Task Tracker API")

menu = st.sidebar.selectbox("Menu", ["Create Task", "View Task", "Update Task",  "Delete Task"])

if menu == "Create Task":
    st.subheader("Create a new Task")
    title = st.text_input("Title")
    description = st.text_area("Description")
    status = st.selectbox("Status", ["Pending", "In Progress", "Completed"])
    priority = st.selectbox("Priority", ["Low", "Medium", "High"])
    due_date = st.date_input("Due Date")
    
    
    if st.button("Create Task"):
        task_data = {"title": title, "description": description, "status": status, "priority": priority, "due_date": str(due_date)}
        response = requests.post(API_url, json=task_data)
        if response.status_code == 201:
            st.success("Task created successfully!")
        else:
            st.error(response.text)
elif menu == "View Task":
    st.header("All Tasks")
    try:
        response = requests.get(API_url)
        if response.status_code == 200:
            tasks = response.json()
            if tasks:
                df = pd.DataFrame(tasks)
                df = df.drop(columns=["id"], errors="ignore")
                df.insert(0, "S.No.", range(1, len(df) + 1))
                #df.index = range(1, len(df) + 1)
                st.dataframe(df, use_container_width=True, hide_index=True)
            else:
                st.info("No tasks Available")
        else:
            st.error("Failed to fetch tasks")
    except Exception as e:
        st.error(f"Connection Error: {e}")
elif menu == "Update Task":

    st.header("Update Task")

    response = requests.get(f"{API_url}/")

    if response.status_code == 200:

        tasks = response.json()

        if tasks:

            # Dropdown mapping
            task_options = {
                f"{index + 1}. {task['title']}": task["id"]
                for index, task in enumerate(tasks)
            }

            selected_task = st.selectbox(
                "Select Task",
                list(task_options.keys())
            )

            task_id = task_options[selected_task]

            selected_task_data = next(
                task for task in tasks
                if task["id"] == task_id
            )

            new_title = st.text_input(
                "New Title",
                value=selected_task_data["title"]
            )

            new_description = st.text_area(
                "New Description",
                value=selected_task_data["description"]
            )

            new_status = st.selectbox(
                "New Status",
                ["Pending", "In Progress", "Completed"],
                index=["Pending", "In Progress", "Completed"].index(
                    selected_task_data["status"]
                )
            )

            new_priority = st.selectbox(
                "New Priority",
                ["Low", "Medium", "High"],
                index=["Low", "Medium", "High"].index(
                    selected_task_data["priority"]
                )
            )

            if st.button("Update Task"):

                payload = {
                    "title": new_title,
                    "description": new_description,
                    "status": new_status,
                    "priority": new_priority
                }

                response = requests.put(
                    f"{API_url}/{task_id}",
                    json=payload
                )

                if response.status_code == 200:
                    st.success("✅ Task updated successfully")
                else:
                    st.error(response.text)

        else:
            st.info("No tasks available")

elif menu == "Delete Task":

    st.header("Delete Task")

    response = requests.get(f"{API_url}/")

    if response.status_code == 200:

        tasks = response.json()

        if tasks:

            # Dropdown mapping
            task_options = {
                f"{index + 1}. {task['title']}": task["id"]
                for index, task in enumerate(tasks)
            }

            selected_task = st.selectbox(
                "Select Task to Delete",
                list(task_options.keys())
            )

            task_id = task_options[selected_task]

            st.warning("This action cannot be undone")

            if st.button("Delete Task"):

                response = requests.delete(
                    f"{API_url}/{task_id}"
                )

                if response.status_code == 200:
                    st.success("✅ Task deleted successfully")
                else:
                    st.error(response.text)

        else:
            st.info("No tasks available")
            

st.sidebar.markdown("---")
st.sidebar.write("Task Tracker App")
