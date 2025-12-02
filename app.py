from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os
from pymongo import MongoClient
from pymongo.errors import PyMongoError

app = Flask(__name__)
# Read-only API that returns data from backend file
DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')

@app.route('/api')
def api():
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
    except Exception as e:
        return jsonify({'error': 'Could not read data file', 'details': str(e)}), 500
    return jsonify(data)

@app.route('/', methods=['GET'])
def index():
    # form page
    return render_template('index.html', error=None, form_data={})

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()

    if not name or not email:
        error = 'Name and email are required.'
        return render_template('index.html', error=error, form_data={'name':name, 'email':email})

    # MongoDB Atlas connection string expected in env var MONGODB_URI
    mongo_uri = os.environ.get('MONGODB_URI')
    if not mongo_uri:
        error = 'Server configuration error: MONGODB_URI not set on server.'
        return render_template('index.html', error=error, form_data={'name':name, 'email':email})

    try:
        client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
        db = client.get_default_database() or client['test']
        collection = db['submissions']
        doc = {'name': name, 'email': email}
        collection.insert_one(doc)
    except PyMongoError as e:
        return render_template('index.html', error=f'MongoDB error: {e}', form_data={'name':name, 'email':email})
    except Exception as e:
        return render_template('index.html', error=f'Unexpected error: {e}', form_data={'name':name, 'email':email})

    return redirect(url_for('success'))

@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
