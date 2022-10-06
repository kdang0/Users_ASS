from flask import Flask
from flask_app.models.user import User
app = Flask(__name__)
app.secret_key = "MAKE IT MAKE SENSE"