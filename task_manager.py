import json
from pathlib import Path
from config import Config


class TaskManager:
    def __init__(self, data_file=None):
        config = Config()
        self.data_file = Path(data_file or config.data_file)
        self.tasks = []
        self.load_tasks()

    def add_task(self, description: str):
        description = description.strip()
        if not description:
            raise ValueError("La descripción de la tarea no puede estar vacía.")

        task = {
            "id": self._next_id(),
            "description": description,
            "completed": False,
        }
        self.tasks.append(task)
        self.save_tasks()
        return task

    def list_tasks(self):
        return self.tasks

    def complete_task(self, task_id: int):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.save_tasks()
                return True
        return False

    def load_tasks(self):
        if not self.data_file.exists():
            self.tasks = []
            return

        try:
            with self.data_file.open("r", encoding="utf-8") as file:
                data = json.load(file)
                self.tasks = data if isinstance(data, list) else []
        except (json.JSONDecodeError, OSError):
            self.tasks = []

    def save_tasks(self):
        with self.data_file.open("w", encoding="utf-8") as file:
            json.dump(self.tasks, file, ensure_ascii=False, indent=4)

    def _next_id(self):
        if not self.tasks:
            return 1
        return max(task["id"] for task in self.tasks) + 1
