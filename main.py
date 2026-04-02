print("Hello! This is a sample project: To-Do App")
import json
from datetime import datetime

class Task:
    def __init__(self, title, completed=False, created_at=None):
        self.title = title
        self.completed = completed
        self.created_at = created_at or datetime.now().isoformat()

    def to_dict(self):
        return {
            "title": self.title,
            "completed": self.completed,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data):
        return Task(
            title=data["title"],
            completed=data["completed"],
            created_at=data["created_at"]
        )


class TodoApp:
    def __init__(self, storage_file="tasks.json"):
        self.storage_file = storage_file
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.storage_file, "r") as f:
                data = json.load(f)
                return [Task.from_dict(task) for task in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self):
        with open(self.storage_file, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            status = "✔" if task.completed else "✘"
            print(f"{i}. [{status}] {task.title} ({task.created_at})")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()


def main():
    app = TodoApp()

    while True:
        print("\n1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task: ")
            app.add_task(title)

        elif choice == "2":
            app.list_tasks()

        elif choice == "3":
            index = int(input("Task number: ")) - 1
            app.complete_task(index)

        elif choice == "4":
            index = int(input("Task number: ")) - 1
            app.delete_task(index)

        elif choice == "5":
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
