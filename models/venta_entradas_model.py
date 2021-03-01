# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class venta_entradas_model(models.Model):
    _name = 'cine.venta_entradas_model'
    _description = 'Modelo de venta de entradas'

    
    
    cantidad = fields.Integer(String="cantidad venta",required=True)
    entrada = fields.Many2one("cine.horario_sala_model")
    venta = fields.Many2one("cine.venta_model")
    
    @api.constrains('venta')
    def Calc_total(self):            
        for r in self:
            r.venta.precio_total += r.cantidad * r.entrada.precio

    @api.constrains('horario_sala_model')
    def actulizaButacas(self):        
        for r in self:
            if r.entrada.butacas_libres < r.cantidad:
                raise ValidationError("No hay suficiente entradas")
            else:
                r.entrada.butacas_libres -=r.cantidad

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
