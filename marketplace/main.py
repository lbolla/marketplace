from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()

# from flask import Flask
# from flask_restplus import Resource, Api

# app = Flask(__name__)
# api = Api(app)

# @api.route('/hello')
# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}

# if __name__ == '__main__':
#     app.run(debug=True)
