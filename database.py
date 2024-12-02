import sqlite3
from database import create_connection

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.status = 'Pendente'

    @staticmethod
    def create_task(task):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)',
                       (task.title, task.description, task.status))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_tasks():
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()
        conn.close()
        return tasks

    @staticmethod
    def update_task(task_id, status):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE tasks SET status = ? WHERE id = ?', (status, task_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_task(task_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
        conn.close()
