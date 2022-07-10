# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 21:37:26 2022

@author: User
"""
from flask_restful import Resource, reqparse, abort, fields, marshal_with

from dataapi1.models.enex_model import ENEXModel 

from dataapi1.database import db


enex_args = reqparse.RequestParser()
enex_args.add_argument("day", type=str, help="Day is required", required=True)
enex_args.add_argument("al_gr", type=str, required=False)
enex_args.add_argument("bg_gr", type=str, required=False)
enex_args.add_argument("mk_gr", type=str, required=False)
enex_args.add_argument("tr_gr", type=str, required=False)
enex_args.add_argument("it_gr", type=str, required=False)
enex_args.add_argument("cr_gr", type=str, required=False)
enex_args.add_argument("gr_al", type=str, required=False)
enex_args.add_argument("gr_bg", type=str, required=False)
enex_args.add_argument("gr_mk", type=str, required=False)
enex_args.add_argument("gr_tr", type=str, required=False)
enex_args.add_argument("gr_it", type=str, required=False)
enex_args.add_argument("gr_cr", type=str, required=False)
enex_args.add_argument("pump", type=str, required=False)
enex_args.add_argument("crete_conventional", type=str, required=False)
enex_args.add_argument("crete_renewables", type=str, required=False)
enex_args.add_argument("big_hydro", type=str, required=False)
enex_args.add_argument("lignite", type=str, required=False)
enex_args.add_argument("natural_gas", type=str, required=False)
enex_args.add_argument("res", type=str, required=False)


resource_fields = {
	'day': fields.String,
    'al_gr' : fields.String,
    'bg_gr' : fields.String,
    'mk_gr' : fields.String,
    'tr_gr' : fields.String,
    'it_gr' : fields.String,
    'cr_gr' : fields.String,
    'gr_al' : fields.String,
    'gr_bg' : fields.String,
    'gr_mk' : fields.String,
    'gr_tr' : fields.String,
    'gr_it' : fields.String,
    'gr_cr' : fields.String,
    'pump' : fields.String,
    'crete_conventional' : fields.String,
    'crete_renewables' : fields.String,
    'big_hydro' : fields.String,
    'lignite' : fields.String,
    'natural_gas' : fields.String,
    'res' : fields.String
}


class ENEX(Resource):
    
    @marshal_with(resource_fields)
    def get(self):
        #epistrefoun ola ta data
        #result = EDAMModel.query.all()
        #print (date)
     
        args = enex_args.parse_args()
        #args['day'] = date
        #print (args)
        result = ENEXModel.query.filter_by(day=args['day']).first()
        if not result:
            abort(404, message="Invalid GET request, result not found")
        return result

    
    @marshal_with(resource_fields)
    def put(self):
        #vazw ena kainourgio pedio.
        args = enex_args.parse_args()
        result = ENEXModel.query.filter_by(day=args['day']).first()
        #print (args,"here")
        if result:
            abort(409, message="Value already exists..")        
            
        entry = ENEXModel(day = args['day'], 
                          al_gr = args['al_gr'],
                          bg_gr = args['bg_gr'],
                          mk_gr = args['mk_gr'],
                          tr_gr = args['tr_gr'],
                          it_gr = args['it_gr'],
                          cr_gr = args['cr_gr'],
                          gr_al = args['gr_al'],
                          gr_bg = args['gr_bg'],
                          gr_mk = args['gr_mk'],
                          gr_tr = args['gr_tr'],
                          gr_it = args['gr_it'],
                          gr_cr = args['gr_cr'],
                          pump = args['pump'],
                          crete_conventional = args['crete_conventional'],
                          crete_renewables = args['crete_renewables'],
                          big_hydro = args['big_hydro'],
                          lignite = args['lignite'],
                          natural_gas = args['natural_gas'],
                          res = args['res'])
        
        db.session.add(entry)
        db.session.commit()
        return entry, 201
        
    '''
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
    '''
