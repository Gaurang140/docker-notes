from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)

# Connect to the MongoDB database
uri = os.getenv('uri')


client = MongoClient(uri)
db = client.todo_db
collection = db.todos

@app.route('/')
def index():
    todos = collection.find()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    todo = request.form.get('todo')
    collection.insert_one({'todo': todo})
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000 ,debug=True)
