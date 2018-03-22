from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, IMAGES

app = Flask(__name__)
app.config['SECRET_KEY'] = "OUR SECRET"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:project1@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning



db = SQLAlchemy(app)


UPLOAD_FOLDER = './app/static/uploads'
app.config.from_object(__name__)
from app import views


