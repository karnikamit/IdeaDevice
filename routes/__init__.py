__author__ = 'karnikamit'
from flask import Flask
import os

proj_path = os.getcwd()
app = Flask(__name__, template_folder=proj_path+"/templates")

from routes import baseroutes
