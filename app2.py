from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask_restful import Resource, Api

app2 = Flask(__name__)

tasks = [ { 'id': 1, 'title': u'Buy groceries', 'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 'done': False }, 
          { 'id': 2, 'title': u'Learn Python', 'description': u'Need to find a good Python tutorial on the web', 'done': False } 
		]

@app2.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET']) 
def get_task(task_id):    
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0 : 
       abort(404) 
    return jsonify({'task': task[0]})

@app2.errorhandler(404) 
def not_found(error): 
    return make_response(jsonify({'error': 'Not found'}), 404)
	
@app2.route('/todo/api/v1.0/tasks', methods=['POST']) 
def create_task(): 
    if not request.json or not 'title' in request.json:        
	       abort(400)    
	       task = {  'id': tasks[-1]['id'] + 1, 
	             'title': request.json['title'],
	             'description': request.json.get('description', ""), 
	             'done': False } 
			 
    tasks.append(task) 
	return jsonify({'task': task}), 201    
#@app2.route('/todo/api/v1.0/tasks', methods=['GET']) 
#def get_tasks(): 
    #return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app2.run(debug=True)