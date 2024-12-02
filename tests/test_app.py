import unittest
import json
from app import app

class TaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_task(self):
        response = self.app.post('/tasks', json={'title': 'Test Task', 'description': 'Test Description'})
        self.assertEqual(response.status_code, 201)

    def test_list_tasks(self):
        response = self.app.get('/tasks')
        self.assertEqual(response.status_code, 200)

    def test_update_task(self):
        response = self.app.put('/tasks/1', json={'status': 'Concluído'})
        self.assertEqual(response.status_code, 200)

    def test_delete_task(self):
        response = self.app.delete('/tasks/1')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
