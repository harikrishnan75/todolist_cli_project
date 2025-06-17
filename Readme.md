# ✅ To-Do List CLI App (Python)

A simple, terminal-based To-Do List application written in Python. This app allows users to add, view, complete, and delete tasks, with data stored persistently in a `tasks.json` file.

---

## 📌 Features

- 📝 Add tasks with title, description, due date, and priority
- 📋 View all saved tasks
- ✅ Mark tasks as completed
- ❌ Delete tasks
- 💾 Persistent storage using a local JSON file
- 🕒 Automatic timestamp for task creation and updates

---

## 📂 File Structure

📁 to_do_list_project/
├── tasks.json # Stores tasks in JSON format
├── to_do.py # Main Python script
└── README.md # Project documentatio





---

## ⚙️ Requirements

- Python 3.7 or above

> No external libraries are needed — only standard Python libraries are used (`json`, `datetime`).

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/to-do-list-cli.git
cd to-do-list-cli



<-- TODOLIST APP MENU -->
1. Add Task
2. Delete Task
3. View Tasks
4. Mark Task as Completed
5. Exit


💡 Example

Edit
Enter your choice: 1
Enter task title: Buy groceries
Enter the task description (optional): Milk, Eggs, Bread
Enter due date (DD-MM-YYYY) (optional): 18-06-2025
Enter priority (Low, Medium, Important): Important
Task added successfully!


📌 Notes
All task data is stored in tasks.json in the same folder as the script.

If tasks.json does not exist, it will be created automatically.

You can reset the app by deleting the tasks.json file.

📜 License
This project is open-source and available under the MIT License.

🙋‍♂️ Author
Harikrishnan D
GitHub Profile Name: harikrishnan75