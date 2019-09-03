from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app, prefix="/api/v1")

tasks = [ { 'id': 1, 'title': u'Buy groceries', 'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 'done': False }, 
          { 'id': 2, 'title': u'Learn Python', 'description': u'Need to find a good Python tutorial on the web', 'done': False } 
		]


class PrivateResource(Resource):
    def get(self):
        return jsonify({'tasks': tasks})

api.add_resource(PrivateResource, '/tasks')

if __name__ == '__main__':
    app.run(debug=True)