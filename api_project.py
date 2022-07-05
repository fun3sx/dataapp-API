# -*- coding: utf-8 -*-
"""
Created on Tue May 17 15:11:43 2022

@author: User
"""

import logging
import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


from flask import Flask, request, abort
from flask_restful import Api
from flask_cors import CORS

from dataapi1.database import db
from dataapi1.resources.hpi_resource import HPI
from dataapi1.resources.gdp_resource import GDP
from dataapi1.resources.unpl_resource import UNPL
from dataapi1.resources.enex_resource import ENEX

from dataapi1.constants import dbloc


logging.basicConfig(
	level=logging.DEBUG,
        format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        datefmt="%m-%d %H:%M",
        handlers=[logging.FileHandler("dataapp_api.log"), logging.StreamHandler()],
    )

app = Flask(__name__)
cors = CORS(app,resources={r'/*':{'origins':'*'}})
app.config["SQLALCHEMY_DATABASE_URI"] = dbloc
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

api = Api(app)

api.add_resource(HPI,"/hpi")
api.add_resource(GDP, "/gdp")
#api.add_resource(GDP,"/gdp",methods=['GET'], endpoint='foo')
api.add_resource(UNPL, "/unpl")
api.add_resource(ENEX, "/enex")


#CORS(app, resources={ r'/*': { 'origins': '*', 'methods': ['GET', 'PUT', 'PATCH']}})
@app.before_request
def before_request_callback():
    if request.method == 'GET' or request.remote_addr == '134.122.55.213' or request.remote_addr == '127.0.0.1':
    	print(request.remote_addr, 'valid request')
        
    else:
        abort(404,'forbidden action')

if __name__ == "__main__":
    #app = create_app(dbloc)
    app.run(host='0.0.0.0',debug=True)