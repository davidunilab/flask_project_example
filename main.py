# pip install -r requirements.txt # install
# pip freeze > requirements.txt # create file
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self, name):
        return {"name": name}

    def put(self, name):
        return {"name": name}

    def delete(self, name):
        return {"name": name}


api.add_resource(HelloWorld, '/read', endpoint="get")
api.add_resource(HelloWorld, '/save/<string:name>', endpoint="post")
# api.add_resource(HelloWorld, '/edit/<string:name>', endpoint="put")
# api.add_resource(HelloWorld, '/remove/<string:name>', endpoint="delete")

if __name__ == '__main__':
    app.run(debug=True, port=8080)
