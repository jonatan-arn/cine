# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class venta_entradas_model(models.Model):
    _name = 'cine.venta_entradas_model'
    _description = 'Modelo de las ventas de entradas'

    id = fields.Integer(String="Id venta entrada",index=True,required=True)
    cantidad_snack= fields.Integer(String="Cantidad de butacas totales de la sala",index=True,required=True)
    snack = fields.Many2one("cine.snacks_model",String="Precio del snack",index=True,required=True)
    precio_total = fields.Float(String="Cantidad total",readonly=True,compute="Calc_total")

    @api.depends('cantidad_snack','snack')
    def Calc_total(self):            
        self.ensure_one
        self.precio_total = self.cantidad_snack * self.snack.precio
        


    
    

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

    
