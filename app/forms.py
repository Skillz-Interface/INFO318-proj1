from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, IntegerField, FileField, SelectField, widgets, BooleanField, RadioField
from wtforms.validators import InputRequired, Length, Regexp, Required
from flask_wtf.file import FileField, FileAllowed, FileRequired






class CreateProfileForm(FlaskForm):
	firstname 		= StringField('First Name', validators 		= [ InputRequired()], render_kw = {'placeholder' : 'First Name'})
	lastname 		= StringField('Last Name', 	validators 		= [ InputRequired()], render_kw = { 'placeholder' : 'Last Name'})
	gender 			= SelectField('Gender Type',choices 		= [('1','FEMALE'), ('2','MALE')], default = '2')
	email           = StringField('Email', validators           = [ InputRequired()],  render_kw = {'placeholder' : '.e.g.getdem@example.com'})
	location        = StringField('Location', validators        = [InputRequired()],  render_kw = {'placeholder' :  'Kingston, Jamaica'})
	biography       = TextAreaField('Biography', validators     = [InputRequired(), Length(max = 200)],  render_kw = {'placeholder': 'Write a short bio', 'rows':'5'})
	photo 			= FileField('Profile Image',validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])


	
