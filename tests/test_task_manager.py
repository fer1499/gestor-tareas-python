import tempfile
import unittest
from pathlib import Path

from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.data_file = Path(self.temp_dir.name) / "test_tasks.json"
        self.manager = TaskManager(self.data_file)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_add_task(self):
        task = self.manager.add_task("Estudiar patrones de diseño")

        self.assertEqual(len(self.manager.list_tasks()), 1)
        self.assertEqual(task["description"], "Estudiar patrones de diseño")
        self.assertFalse(task["completed"])
        self.assertTrue(self.data_file.exists())

    def test_complete_task(self):
        task = self.manager.add_task("Ejecutar pruebas unitarias")
        result = self.manager.complete_task(task["id"])

        self.assertTrue(result)
        self.assertTrue(self.manager.list_tasks()[0]["completed"])

    def test_complete_nonexistent_task(self):
        self.assertFalse(self.manager.complete_task(999))


if __name__ == "__main__":
    unittest.main()
