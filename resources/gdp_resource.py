# -*- coding: utf-8 -*-
"""
Created on Wed May 18 12:21:36 2022

@author: User
"""
from flask_restful import Resource, reqparse, abort, fields, marshal_with

from dataapi1.models.gdp_model import GDPModel 

from dataapi1.database import db


gdp_args = reqparse.RequestParser()
gdp_args.add_argument("quarter", type=str, help="Quarter in question is required", required=True)
gdp_args.add_argument("value", type=str, help="Value is required", required=True)


resource_fields = {
	'quarter': fields.String,
	'value': fields.String,
}


class GDP(Resource):
    
    @marshal_with(resource_fields)
    def get(self):
        #epistrefoun ola ta data
        result = GDPModel.query.all()
        if not result:
            abort(404, message="Invalid GET request")
        return result

    
    @marshal_with(resource_fields)
    def put(self):
        #vazw ena kainourgio pedio.
        args = gdp_args.parse_args()
        result = GDPModel.query.filter_by(quarter=args['quarter']).first()
        
        if result:
            abort(409, message="Value already exists..")        
            
        entry = GDPModel(quarter=args['quarter'], value=args['value'])
        db.session.add(entry)
        db.session.commit()
        return entry, 201
        

    @marshal_with(resource_fields)
    def patch(self):
        #kanw update ena pedio
        args = gdp_args.parse_args()
        result = GDPModel.query.filter_by(quarter=args['quarter']).first()
        if not result:
            abort(404, message="entry does not exist, cannot update")  
        result.quarter = args['quarter']
        result.value = args['value']
        db.session.commit()
        return result
    
