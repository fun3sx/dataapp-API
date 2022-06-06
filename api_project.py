# -*- coding: utf-8 -*-
"""
Created on Tue May 17 15:11:43 2022

@author: User
"""

import logging
import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


from flask import Flask
from flask_restful import Api

from dataapi1.database import db
from dataapi1.resources.hpi_resource import HPI
from dataapi1.resources.gdp_resource import GDP

from dataapi1.constants import dbloc


logging.basicConfig(
	level=logging.DEBUG,
        format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        datefmt="%m-%d %H:%M",
        handlers=[logging.FileHandler("dataapp_api.log"), logging.StreamHandler()],
    )

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = dbloc
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

api = Api(app)

api.add_resource(HPI,"/hpi")
api.add_resource(GDP,"/gdp")





if __name__ == "__main__":
    #app = create_app(dbloc)
    app.run(host='0.0.0.0')
