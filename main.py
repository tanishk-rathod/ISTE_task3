from flask import Flask,render_template,request,session,redirect,flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from datetime import datetime
import os,json,math
from data import data

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo



app = Flask(__name__)
app.secret_key = 'secret key'




class editForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    year = StringField(validators=[DataRequired()])
    vertical = StringField(validators=[DataRequired()])
    linkedinProfile = StringField()
    instagramProfile = StringField()
    facebookProfile = StringField()
    photo = StringField(validators=[DataRequired()])
    submit = SubmitField('Submit')




@app.route("/", methods=['GET', 'POST'])
def cards():
    return render_template("cards.html", data=data)


@app.route("/card/<string:sno>")
def card(sno):
    for card in data:
        if card['S_no']==sno:
            break
    return render_template('card.html', card=card)




@app.route("/edit/<string:sno>", methods=['GET', 'POST'])
def edit(sno):
    form = editForm()
    for card in data:
        if card['S_no']==sno:
            break
    
    if(request.method=="POST"):
        card['timestamp']=datetime.utcnow()
        card['name']=form.name.data
        card['year']=form.year.data
        card['vertical']=form.vertical.data
        card['linkedinProfile']=form.linkedinProfile.data
        card['instagramProfile']=form.instagramProfile.data
        card['facebookProfile']=form.facebookProfile.data
        card['photo']=form.photo.data
        return redirect('/')

    return render_template("edit.html",card=card,form=form)






app.run(debug=True)
