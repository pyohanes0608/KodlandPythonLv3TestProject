# tests/test_add_task.py
import unittest
from database import init_db, add_task_to_db, get_all_tasks

class TestAddTask(unittest.TestCase):
    def setUp(self):
        init_db()

    def test_add_task(self):
        task_description = "Test task 1"
        task_id = add_task_to_db(task_description)
        tasks = get_all_tasks()
        self.assertTrue(any(task[0] == task_id and task[1] == task_description for task in tasks))

if __name__ == "__main__":
    unittest.main()
