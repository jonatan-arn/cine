# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class venta_snack_model(models.Model):
    _name = 'cine.venta_snack_model'
    _description = 'Modelo de venta de snacks'

    
    
    cantidad = fields.Integer(String="cantidad venta",required=True)
    snack = fields.Many2one("cine.snacks_model")
    venta = fields.Many2one("cine.venta_model")
    
    @api.constrains('venta')
    def Calc_total(self):            
        for r in self:
            r.venta.precio_total += r.cantidad * r.snack.precio

    @api.constrains('snack')
    def actulizaStock(self):        
        for r in self:
            if r.snack.stock < r.cantidad:
                raise ValidationError("No hay suficiente stock")
            else:
                r.snack.stock -=r.cantidad

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
