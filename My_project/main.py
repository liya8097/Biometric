from flask import Flask, request
import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext
import os
from flask.templating import render_template 

app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def index():
  return render_template('index.html')
# @app.route('/attendance')   
# def attend(): 


if __name__=="__main__":
 app.run(debug=True)

