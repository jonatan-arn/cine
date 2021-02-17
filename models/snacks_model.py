# -*- coding: utf-8 -*-

from odoo import models, fields, api


class snacks_model(models.Model):
    _name = 'cine.snacks_model'
    _description = 'Modelo de snacks'

    
    name= fields.Char(String="Nombre del snack",index=True,required=True)
    precio = fields.Integer(String="Precio de la butaca",index=True,required=True)
    stock = fields.Float(String="Cantidad de stock",readonly=True,default=0)


    
    
    

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
