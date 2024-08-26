from flask import Flask, jsonify, request


app = Flask(__name__)


tasks = [
    {
        'id': 1,
        'title': 'Learn Flask',
        'description': 'Get familiar with Flask Framework',
        'done': False
    },
    {
        'id': 2,
        'title': 'Build an API',
        'description': 'Create a basic API using Flask',
        'done': False 
    }
]


@app.route('/')
def home():
    return "Hello, Flask!"


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})  # Returns the list of tasks


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return jsonify({'task': task})
    else:
        return jsonify({'message': 'Task not found'}), 404


@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        return jsonify({'message': 'Title is required'}), 400

    new_task = {
        'id': tasks[-1]['id'] + 1 if tasks else 1,  # Generates a new ID based on the last task's ID
        'title': request.json['title'],
        'description': request.json.get('description', ""),  # Empty string if no description is provided
        'done': False
    }
    tasks.append(new_task)
    return jsonify({'task': new_task}), 201  # Returns the created task with a 201 status code


@app.route('/tasks/<int:task_id>', methods=['PATCH']) # Used for partial updates
def update_task_partial(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if not task:
        return jsonify({'message': 'Task not found'}), 404

    if not request.json:  # Checks if the request contains JSON data
        return jsonify({'message': 'Bad request, JSON data is required'}), 400

    # Update the task fields if they are provided in the request
    task['title'] = request.json.get('title', task['title'])
    task['description'] = request.json.get('description', task['description'])
    task['done'] = request.json.get('done', task['done'])

    return jsonify({'task': task})


@app.route('/tasks/search,', methods=['GET'])
def search_tasks():
    query = request.args.get('q', "") # Gets the search query from the URL parameters
    matching_tasks = [task for task in tasks if query.lower() in task['title'].lower() or query.lower() in task['description'].lower()]
    return jsonify({'tasks': matching_tasks}) if matching_tasks else jsonify({'message': 'No tasks found'}), 404 


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'message': 'Task not found'}), 404

    tasks.remove(task)
    return jsonify({'message': 'Task deleted successfully'}), 200


if __name__ == '__main__':
    app.run(debug=True)
