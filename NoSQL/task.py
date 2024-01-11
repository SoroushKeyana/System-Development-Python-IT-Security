import pymongo 
import PySimpleGUI as sg

# Connect to MongoDB 
client = pymongo.MongoClient("mongodb://localhost:27017/") 
database = client["mydb"]
task_collection = database["tasks"] 

# Create a task 
def add_task(task_title, task_description, task_status="To Do"): 
    task = {"title": task_title, "description": task_description, "status": task_status}
    task_collection.insert_one(task) 

# List all tasks
def list_tasks(): 
    cursor = task_collection.find()
    for task in cursor:
        print(task) 

# Change the status of a task 
def update_task_status(task_title, new_status): 
    task_collection.update_one({"title": task_title},{"$set": {"status": new_status}}) 

# Delete a task
def delete_task(task_title): 
    task_collection.delete_one({"title": task_title})

list_tasks()


# Create a GUI window
window = sg.Window("Task Manager", layout=[[sg.Text("Task Title"), sg.InputText(key="task_title")],
                                           [sg.Text("Task Description"), sg.InputText(key="task_description", size=(50, 5))],
                                           [sg.Button("Add Task"), sg.Button("List Tasks"), sg.Button("Update Task Status"), sg.Button("Delete Task")],
                                           [sg.Output(key="output")]])

# Event loop
while True:
    event, values = window.read()

    if event == "Add Task":
        task_title = values["task_title"]
        task_description = values["task_description"]

        add_task(task_title, task_description)

        window.update("output", "Task created successfully.")

    elif event == "List Tasks":
        list_tasks()

        window.update("output", "Tasks listed successfully.")

    elif event == "Update Task Status":
        task_title = values["task_title"]
        new_status = values["new_status"]

        update_task_status(task_title, new_status)

        window.update("output", "Task status updated successfully.")

    elif event == "Delete Task":
        task_title = values["task_title"]

        delete_task(task_title)

        window.update("output", "Task deleted successfully.")

    elif event == sg.WIN_CLOSED:
        break

# Close the GUI window
window.close()
