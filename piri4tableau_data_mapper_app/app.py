from flask_sqlalchemy import SQLAlchemy
import os
from flask import (Flask, render_template, redirect, jsonify, request)
from flask_pymongo import PyMongo
import json
from Pay_stub import Pay_stub, Employee_form_data, ModGeneratedPayStubFrom
from flask_wtf import FlaskForm  
from forms import ContactForm, Timesheet, Tim3sheet, EmployeeForm 
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
