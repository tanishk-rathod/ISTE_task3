from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo




class RegistrationForm(FlaskForm):
    name = StringField(
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField(
                        validators=[DataRequired(), Email()])
    phone = StringField(
                        validators=[DataRequired(), Length(10)])
    college = StringField(validators=[Length(max=10)])
    city = StringField(
                        validators=[DataRequired(), Length(20)])
    state = StringField(
                        validators=[DataRequired(), Length(20)])
    no_of_members = IntegerField(validators=[DataRequired(), Length(3)])

    submit = SubmitField('Register')



class ContactForm(FlaskForm):
    name = StringField(
                        validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField(
                        validators=[DataRequired(), Email()])
    phone = StringField(
                        validators=[DataRequired(), Length(10)])
    subject = StringField(
                           validators=[DataRequired(), Length(min=2, max=50)])
    message = StringField(
                           validators=[DataRequired(), Length(min=2, max=200)])
    submit = SubmitField('Send Message')







