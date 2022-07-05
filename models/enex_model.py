# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 21:31:47 2022

@author: User
"""

from dataapi1.database import db

class ENEXModel(db.Model):
    day = db.Column(db.String(100), nullable=False,primary_key=True)
    al_gr = db.Column(db.String(), nullable=True)
    bg_gr = db.Column(db.String(), nullable=True)
    mk_gr = db.Column(db.String(), nullable=True)
    tr_gr = db.Column(db.String(), nullable=True)
    it_gr = db.Column(db.String(), nullable=True)
    cr_gr = db.Column(db.String(), nullable=True)
    gr_al = db.Column(db.String(), nullable=True)
    gr_bg = db.Column(db.String(), nullable=True)
    gr_mk = db.Column(db.String(), nullable=True)
    gr_tr = db.Column(db.String(), nullable=True)
    gr_it = db.Column(db.String(), nullable=True)
    gr_cr = db.Column(db.String(), nullable=True)
    pump = db.Column(db.String(), nullable=True)
    crete_conventional = db.Column(db.String(), nullable=True)
    crete_renewables = db.Column(db.String(), nullable=True)
    big_hydro = db.Column(db.String(), nullable=True)
    lignite = db.Column(db.String(), nullable=True)
    natural_gas = db.Column(db.String(), nullable=True)
    res = db.Column(db.String(), nullable=True)
        
    
    

    def __repr__(self):
        return f"Entry(day = {day}, al_gr = {al_gr}, bg_gr = {bg_gr}, mk_gr = {mk_gr}, tr_gr = {tr_gr}, it_gr = {it_gr}, cr_gr = {cr_gr}, gr_al = {gr_al}, gr_bg = {gr_bg}, gr_mk = {gr_mk}, gr_it = {gr_it}, gr_tr = {gr_tr}, gr_cr = {gr_cr}, pump = {pump}, crete_conventional = {crete_conventional}, crete_renewables = {crete_renewables}, big_hydro = {big_hydro}, lignite = {lignite}, natural_gas = {natural_gas}, res = {res} )"
    
    
    