from flask import Flask,render_template,request,session,redirect,flash
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from datetime import datetime
import os,json,math
import psycopg2.extras
import psycopg2 




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:tanishk%40123@localhost/iste3'
app.secret_key = 'secret key'


db=SQLAlchemy(app)

from models import Contact, Register
from forms import RegistrationForm, ContactForm

@app.route("/")
def home():
    return render_template("index.html", page=1)

@app.route("/contact", methods=['GET','POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        entry = Contact(Name=form.name.data,Email=form.email.data,Phone=form.phone.data,Subject=form.subject.data,Message=form.message.data)
        db.session.add(entry)
        db.session.commit()
        return redirect('/') 
    return render_template('contact.html',page=4, form=form)

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        entry = Register(Name=form.name.data, Email=form.email.data, Phone=form.phone.data, College=form.college.data, City=form.city.data, State=form.state.data, No_of_members=form.no_of_members.data)
        print(entry)
        db.session.add(entry)
        db.session.commit()
        # print(form.name.data)
        return redirect('/') 
    return render_template('register.html', form=form)


@app.route("/about")
def about():
    return render_template('about.html', page=2)

@app.route("/speakers")
def speakers():
    return render_template('speakers.html', page = 3)

@app.route("/aboutted")
def aboutted():
    return render_template('aboutted.html')




app.run(debug=True, port=8000)

