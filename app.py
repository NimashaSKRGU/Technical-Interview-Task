from flask import Flask, session, request, render_template, jsonify
import requests
import pandas as pd
import json
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_urlsafe(10)


def sort_items(list):
    return sorted(list, key=lambda k: k['id'])


@app.before_request
def load_data():
    # Load the session data if not available
    if session.get("item_data") is None:
        preload()


@app.route('/')
def index():
    data = json.loads(session.get('item_data'))
    sorted_data = sort_items(data)
    df = pd.read_json(json.dumps(sorted_data))
    return render_template('index.html', data=df)


@app.route('/preload')
def preload():
    json_url = 'https://gist.githubusercontent.com/chamathpali/7cccd0ff8a0338645559e5ed468231fa/raw/3a467ff8807a090cbdbe5e4583b8d07b925a7979/items.json'
    try:
        uri_response = requests.get(json_url)
    except requests.ConnectionError:
        return "Connection Error"
    item_data = uri_response.json()
    session['item_data'] = json.dumps(item_data)
    return jsonify(item_data)


@app.route('/items', methods=['GET'])
def list():
    return session.get('item_data')


@app.route('/items', methods=['POST'])
def add_items():
    list = session.get('item_data')
    json_list = json.loads(list)
    obj_to_append = {
        'id': json_list[-1]['id'] + 1,
        'name': request.form['fname'],
        'price': request.form['fprice'],
        'quantity': request.form['fqty']
    }

    json_list.append(dict(obj_to_append))  # append data
    json_list = sort_items(json_list)
    session['item_data'] = json.dumps(json_list)
    return jsonify(json_list)


@app.route('/items/<int:id>', methods=['DELETE'])
def delete_items(id=0):
    list = session.get('item_data')
    json_list = json.loads(list)
    sorted_list = sort_items(json_list)
    sorted_list = [x for x in sorted_list if x['id'] != id]
    session['item_data'] = json.dumps(sorted_list)
    return jsonify(sorted_list)


if __name__ == '__main__':
    app.run()
