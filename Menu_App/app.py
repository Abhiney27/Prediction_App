from flask import Flask
from flask import render_template
from flask import request
import subprocess
import joblib
from colorama import Fore
import getpass
import time
import os
import webbrowser

app = Flask("Menu_App")
@app.route("/home")
def home():
	return(render_template("myhome.html"))

@app.route("/menu")
def menu():
	myname = request.args.get("name")
	mysurname = request.args.get("surname")
	htmlcode = render_template("mymenu.html" , name= myname , surname= mysurname)
	return(htmlcode)

@app.route("/cmnd")
def cmnd():
	myname = request.args.get("name")
	mysurname = request.args.get("surname")
	code = render_template("mycmnd.html" , name= myname , surname= mysurname)
	return(code)

@app.route("/house_menu")
def house():
	myname = request.args.get("name")
	mysurname = request.args.get("surname")
	house_code = render_template("myhouse.html" , name= myname , surname= mysurname)
	return(house_code)

@app.route("/salary")
def salary_predict():
	exp = float(request.args.get("years"))
	model = joblib.load("salary_model.pk2")
	mysalary  = str(model.predict([[exp]])[0])
	result = render_template("salary.html" , years = exp , salary = mysalary )
	if exp>70:
		return("<br>"  + "There is no chance that anybody has that much experience..., if u have then you might be Alien..." + "</b>")
	return(result)

@app.route("/cmnd_run")
def run_cmnd():
	cmnd = request.args.get("cmnd")
	return("<b>" + "<pre>" + subprocess.getoutput(cmnd) + "</pre>" + "</b>")

@app.route("/house_price")
def house_predict():
	myincome = float(request.args.get("income"))
	myhouse_age = float(request.args.get("house_age"))
	myroom = float(request.args.get("room"))
	mybed_room = float(request.args.get("bed_room"))
	mypopulation = float(request.args.get("population"))
	model = joblib.load('housemodel.pk1')
	myprice = str(round(model.predict([[myincome , myhouse_age , myroom , mybed_room , mypopulation]])[0]))
	result = render_template("house_price.html" , income = myincome , house_age = myhouse_age , room = myroom , bed_room = mybed_room , population = mypopulation  , price = myprice )
	return(result)

app.run(host='127.0.0.1', port=3000)
