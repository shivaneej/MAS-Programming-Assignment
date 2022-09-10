import collections
import json
from turtle import pos
from flask import Flask, request
import firebase_admin
from firebase_admin import credentials, db

FIREBASE_URL = 'https://mas-programming-9f4f3-default-rtdb.firebaseio.com/'
PATH_TO_SERVICE_ACC_KEY = 'mas-programming-9f4f3-firebase-adminsdk-ir27a-0a40c33de8.json'

app = Flask(__name__)

cred = credentials.Certificate(PATH_TO_SERVICE_ACC_KEY)
firebase_admin.initialize_app(cred, {'databaseURL' : FIREBASE_URL})
ref = db.reference('/posts')

@app.route('/posts', methods=['GET'])
def query_posts():
    posts = ref.order_by_child('timestamp').get()
    posts = collections.OrderedDict(reversed(list(posts.items())))    
    return posts

@app.route('/posts', methods=['POST'])
def create_post():
    request_data = json.loads(request.data)
    post_info = {
        'name': request_data['name'],
        'description': request_data['description'],
        'price': request_data['price'],
        'category': request_data['category'],
        'image_url': request_data['image_url'],
        'mobile': request_data['mobile'],
        'timestamp': {'.sv': 'timestamp'}
    }
    ref.push().set(post_info)
    return post_info


@app.route('/health')
def index():
    return 'Service is up!'

app.run(debug=True)
