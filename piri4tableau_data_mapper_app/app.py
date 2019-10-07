import os
from flask import (Flask, render_template, redirect, jsonify, request)
import json
from flask_wtf import FlaskForm  
app = Flask(__name__)
flask_debug = False
app.config['FLASK_DEBUG'] = flask_debug
app.config['WTF_CSRF_ENABLED'] = False

@app.route('/')
def index():
    return render_template('home4XMLparser.html')

# ============ THE END ==============
if __name__ == '__main__':
  app.run(debug=True)
