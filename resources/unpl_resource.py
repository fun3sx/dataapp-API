# -*- coding: utf-8 -*-
"""
Created on Wed May 18 12:21:36 2022

@author: User
"""
from flask_restful import Resource, reqparse, abort, fields, marshal_with

from dataapi1.models.unpl_model import UNPLModel 

from dataapi1.database import db


unpl_args = reqparse.RequestParser()
unpl_args.add_argument("month", type=str, help="Month in question is required", required=True)
unpl_args.add_argument("value", type=str, help="Value is required", required=True)


resource_fields = {
	'month': fields.String,
	'value': fields.String,
}


class UNPL(Resource):
    
    @marshal_with(resource_fields)
    def get(self):
        #epistrefoun ola ta data
        result = UNPLModel.query.all()
        if not result:
            abort(404, message="Invalid GET request")
        return result

    
    @marshal_with(resource_fields)
    def put(self):
        #vazw ena kainourgio pedio.
        args = unpl_args.parse_args()
        result = UNPLModel.query.filter_by(month=args['month']).first()
        
        if result:
            abort(409, message="Value already exists..")        
            
        entry = UNPLModel(month=args['month'], value=args['value'])
        db.session.add(entry)
        db.session.commit()
        return entry, 201
        

    @marshal_with(resource_fields)
    def patch(self):
        #kanw update ena pedio
        args = unpl_args.parse_args()
        result = UNPLModel.query.filter_by(month=args['month']).first()
        if not result:
            abort(404, message="entry does not exist, cannot update")  
        result.quarter = args['month']
        result.value = args['value']
        db.session.commit()
        return result
    
