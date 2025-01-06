# tests/test_show_tasks.py
import unittest
from database import init_db, add_task_to_db, get_all_tasks

class TestShowTasks(unittest.TestCase):
    def setUp(self):
        init_db()

    def test_show_tasks(self):
        add_task_to_db("Task 1")
        add_task_to_db("Task 2")
        tasks = get_all_tasks()
        self.assertGreaterEqual(len(tasks), 2)

if __name__ == "__main__":
    unittest.main()
