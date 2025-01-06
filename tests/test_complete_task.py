# tests/test_complete_task.py
import unittest
from database import init_db, add_task_to_db, mark_task_as_completed, get_all_tasks

class TestCompleteTask(unittest.TestCase):
    def setUp(self):
        init_db()

    def test_complete_task(self):
        task_description = "Task to complete"
        task_id = add_task_to_db(task_description)
        rows_updated = mark_task_as_completed(task_id)
        tasks = get_all_tasks()
        self.assertEqual(rows_updated, 1)
        self.assertTrue(any(task[0] == task_id and task[2] == 1 for task in tasks))

if __name__ == "__main__":
    unittest.main()
