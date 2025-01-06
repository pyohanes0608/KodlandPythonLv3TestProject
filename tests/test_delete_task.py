# tests/test_delete_task.py
import unittest
from database import init_db, add_task_to_db, delete_task_from_db, get_all_tasks

class TestDeleteTask(unittest.TestCase):
    def setUp(self):
        init_db()

    def test_delete_task(self):
        task_description = "Task to delete"
        task_id = add_task_to_db(task_description)
        rows_deleted = delete_task_from_db(task_id)
        tasks = get_all_tasks()
        self.assertEqual(rows_deleted, 1)
        self.assertFalse(any(task[0] == task_id for task in tasks))

if __name__ == "__main__":
    unittest.main()
