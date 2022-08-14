# -*- coding: utf-8 -*-
"""
Created on Wed May 18 12:21:36 2022

@author: User
"""
from flask_restful import Resource, reqparse, abort, fields, marshal_with

from dataapi1.models.mortgageOrigination_model import MortgageModel 

from dataapi1.database import db


mortgageOrigination_args = reqparse.RequestParser()
mortgageOrigination_args.add_argument("month", type=str, help="Month in question is required", required=True)
mortgageOrigination_args.add_argument("value", type=str, help="Value is required", required=True)


resource_fields = {
	'month': fields.String,
	'value': fields.String,
}


class MortgageOrigination(Resource):
    
    @marshal_with(resource_fields)
    def get(self):
        #epistrefoun ola ta data
        result = MortgageModel.query.all()
        if not result:
            abort(404, message="Invalid GET request")
        return result

    
    @marshal_with(resource_fields)
    def put(self):
        #vazw ena kainourgio pedio.
        args = mortgageOrigination_args.parse_args()
        result = MortgageModel.query.filter_by(month=args['month']).first()
        
        if result:
            abort(409, message="Value already exists..")        
            
        entry = MortgageModel(month=args['month'], value=args['value'])
        db.session.add(entry)
        db.session.commit()
        return entry, 201
        

    @marshal_with(resource_fields)
    def patch(self):
        #kanw update ena pedio
        args = mortgageOrigination_args.parse_args()
        result = MortgageModel.query.filter_by(month=args['month']).first()
        if not result:
            abort(404, message="entry does not exist, cannot update")  
        result.quarter = args['month']
        result.value = args['value']
        db.session.commit()
        return result
    
