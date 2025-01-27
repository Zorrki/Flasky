import datetime
import os
from flask import Flask

app = Flask(__name__)

@app.route('/hello/<username>')
def hello_world(username):
    return f'Привет, {username}!'

@app.route('/even/<int:number>')
def even(number: int):
    if number % 2 == 0:
        res = 'odd number'
    else:
        res = 'even number'
    return f'{number} is <b>{res}</b>'

@app.route('/compare/<float:number_1>/<float:number_2>')
def compare(number_1: float, number_2: float):
    if number_1 > number_2:
        result = '>'
    elif number_1 < number_2:
        result = '<'
    else:
        result = '='
    return f'<h3>Compare</h3> {number_1} {result} {number_2}'

import os
from flask import Flask

app = Flask(__name__)

@app.route('/check_exists/<path:file_path>')
def check_exists(file_path: str):
    """
    Check if a file with a relative path exists in the filesystem.
    :param file_path: the relative path
    :return: HTTP response indicating whether the file exists
    """
    print(f'File path is {file_path}')
    # Define the base directory relative to which the search will be performed
    base_dir = '/Users/azkarpenko/GB_PY_ADV/flask_2'
    # Convert the relative path to an absolute path
    absolute_path = os.path.join(base_dir, file_path)
    
    # Check if the file exists
    file_exists = os.path.exists(absolute_path)
    result = 'exists' if file_exists else 'does not exist'
    status_code = 200 if file_exists else 404

    return f'File <h3>{file_path}</h3> {result}', status_code

if __name__ == '__main__':
    app.run(debug=True)