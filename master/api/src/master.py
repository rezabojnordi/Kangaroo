
#!flask/bin/python
from flask import Flask
import os
from flask import jsonify,json


app = Flask(__name__)


class Kangero():

    def __init__(self,instance_id):
        self.instance_id =instance_id
        


