from flask import Flask, request, jsonify
from models import Task
from database import create_table

app = Flask(__name__)
create_table()

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task = Task(data['title'], data['description'])
    Task.create_task(task)
    return jsonify({"message": "Tarefa criada com sucesso!"}), 201

@app.route('/tasks', methods=['GET'])
def list_tasks():
    tasks = Task.get_all_tasks()
    return jsonify(tasks), 200

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    Task.update_task(task_id, data['status'])
    return jsonify({"message": "Tarefa atualizada com sucesso!"}), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    Task.delete_task(task_id)
    return jsonify({"message": "Tarefa deletada com sucesso!"}), 204

if __name__ == '__main__':
    app.run(debug=True)
