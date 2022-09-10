import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/posts', methods=['GET'])
def query_posts():
    posts = [1, 2, 3]
    return posts

@app.route('/posts', methods=['POST'])
def create_post():
    post_info = json.loads(request.data)
    return post_info


@app.route('/health')
def index():
    return 'Service is up!'

app.run(debug=True)
