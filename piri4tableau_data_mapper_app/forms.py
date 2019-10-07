from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError

class ContactForm(FlaskForm):
   name = TextField("Name Of Student", [validators.Required("Please enter your name.")])
   Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
   Address = TextAreaField("Address")
   email = TextField("Email",[validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
   Age = IntegerField("age")
   language = SelectField('Languages', choices = [('cpp', 'C++'), ('py', 'Python')])
   submit = SubmitField("Send")

class Timesheet(FlaskForm):
   hh_in = IntegerField(default = '10')
   mm_in = IntegerField(default = '00')
   ampm_in = SelectField(choices = [('AM', 'a'), ('PM', 'p' )])
   hh_out = IntegerField(default = "09")
   mm_out = IntegerField(default = "00")
   ampm_out = SelectField(choices = [('PM','p'), ('AM','a')])
   submit = SubmitField("Send")
   # min_total_in = (int(hh_in) * 60) + mm_in
   # min_total_out = (hh_out * 60) + mm_out
   # total_hours =  (min_total_out - min_total_in)*1/60 

class Tim3sheet(Timesheet):
   def __init__(self, label = 'no_label_set'):
      pass
      self.label = label

class EmployeeForm(FlaskForm):
   name_ee = TextField("Name Of Employee", [validators.Required("Please enter your name.")])
   name_er = TextField("Name Of Employee", [validators.Required("Please enter your name.")])
   address_ee = TextAreaField("Employee Address")
   address_er = TextAreaField("Company Address")
   Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
   allowance = IntegerField("allowance")
   frequency = SelectField('Frequency', choices = [('biweekly', 'monthly'), ('bw', 'mo')])
   submit = SubmitField("Send")
