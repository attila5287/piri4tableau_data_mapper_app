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

# only use when uploading to heroku-config var is dynamic for postgres
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"

db = SQLAlchemy(app)

# # ===================== DEFINE DATABASE MODEL ======================
class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(64))
    middleName = db.Column(db.String(64))
    lastName = db.Column(db.String(64))
    companyName = db.Column(db.String(64))
    allowance = db.Column(db.Integer)
    hourlyRate = db.Column(db.Float)
    hoursWorked = db.Column(db.Float)

    def __repr__(self):
        return '<Employee %r %r>' % (self.firstName, self.lastName) 

class Employe3():
    def __init__(self, 
                 firstName = 'Abuzer',
                 middleName = 'B',
                 lastName = 'Kadayif' ,
                 companyName = 'Baklava LLC',
                 hourlyRate = 14.33,
                 hoursWorked = 80.00
                ):
        pass
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.companyName = companyName
        self.hourlyRate = hourlyRate
        self.hoursWorked = hoursWorked
    def __str__(self):
        msg = 'dummy object created'
        return msg


@app.route('/')
def index():
    return render_template('home4XMLparser.html')


@app.route('/intro')
def ind3x():
    return render_template('home.html')

# Query the database and send the jsonified results
@app.route("/send", methods=["GET", "POST"]) 
def send():
    if request.method == "POST":
        employee = Employee(
            firstName = request.form["firstName"],
            middleName = request.form["middleName"],
            lastName=request.form["lastName"],
            companyName = request.form["companyName"],
            allowance = request.form["allowance"],
            hourlyRate = request.form["hourlyRate"],
            hoursWorked=request.form["hoursWorked"]
            )

        db.session.add(employee)
        db.session.commit()
        user_input = Employee_form_data(
            firstName = request.form["firstName"],
            middleName = request.form["middleName"],
            lastName=request.form["lastName"],
            companyName = request.form["companyName"],
            allowance = request.form["allowance"],
            hourlyRate = request.form["hourlyRate"],
            hoursWorked=request.form["hoursWorked"]
        )

        generated_paystub = ModGeneratedPayStubFrom(
            firstName = request.form["firstName"],
            middleName = request.form["middleName"],
            lastName=request.form["lastName"],
            companyName = request.form["companyName"],
            allowance = int(request.form["allowance"]),
            hourlyRate = float(request.form["hourlyRate"]),
            hoursWorked= float(request.form["hoursWorked"]),
            payCntYr2Dt= int(request.form["payCntYr2Dt"]),
            dateStart=request.form["dateStart"],
            dateEnd=request.form["dateEnd"]
        )
        dict = {
        'Social Security' : float(generated_paystub.social_security_perc), 
        'Medicare' : float(generated_paystub.medicare_perc), 
        'Total Taxes Withheld From Employee': float(generated_paystub.taxes_perc),
        'Net Pay': float(generated_paystub.net_pay_perc)
        # 'FUTA' : float(generated_paystub.futa_perc), 
        # 'State Unemployment Tax' : float(generated_paystub.co_unemp_perc) 
        }
    
        return render_template("pay_stub_generat0r.html", Pay_stub=generated_paystub, dict = dict)
        
    return render_template("form.html")

# ====   ==================  ======================
@app.route("/api/pals")
def pals():
   results = db.session.query(Employee.lastName, Employee.firstName, Employee.middleName, Employee.allowance, Employee.hourlyRate, Employee.hoursWorked).all()

   firstName = [result[0] for result in results]
   middleName = [result[1] for result in results]
   lastName = [result[2] for result in results]
   allowance = [result[3] for result in results]
   hourlyRate = [result[4] for result in results]
   hoursWorked = [result[5] for result in results]
   ee_data = [{
         'firstName' : firstName,
         'middleName' : middleName,
         'lastName' : lastName,
         'allowance' : allowance,
         'hourlyRate' : hourlyRate,
         'hoursWorked' : hoursWorked
   }]
   return jsonify(ee_data)
# ============================================
@app.route('/eeinfo', methods = ['GET', 'POST']) 
def cont4ct():
   pass
   form = EmployeeForm()
   if request.method == 'POST':
      if form.validate() == False:
         return render_template('forms_employee.html', form=form)
   elif request.method == 'GET':
      return render_template('forms_employee.html', form=form)
   else:
      return render_template('form_data_employee.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      print(result)
      return render_template("form_data_employee.html", result=result)

@app.route('/timesheet', methods = ['POST', 'GET'])
def Tim3sheet_first_week():
    pass
    days_list = ['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat', 'Sun']
    forms_l1st = [
      Timesheet(day) for day in days_list
    ]
    if request.method == 'POST':
        result = request.form
        print(result)

    return render_template('forms_timesheet.html', forms_list = forms_l1st)

@app.route('/paystubviewer')
def Pay_stub_generet0r():
    pass
    tes2t_a_paystub = Pay_stub()
    return render_template('pay_stub_viewer.html', Pay_stub = test_a_paystub)

@app.route('/contact', methods = ['POST', 'GET'])
def contact():
   pass
   form = ContactForm()
   if request.method == 'POST':
      pass
      result = request.form
      print(result)
      return render_template("result.html", result=result)
   return render_template('contact.html', form = form)

# ============ THE END ==============
if __name__ == '__main__':
  app.run(debug=True)