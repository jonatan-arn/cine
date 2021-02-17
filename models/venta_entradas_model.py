# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class venta_entradas_model(models.Model):
    _name = 'cine.venta_entradas_model'
    _description = 'Modelo de las ventas de entradas'

    id = fields.Integer(String="Id venta entrada",index=True,required=True)
    cantidad_butacas= fields.Integer(String="Cantidad de butacas totales de la sala",index=True,required=True)
    butaca = fields.Many2one("cine.horario_sala_model",String="Precio de la butaca",index=True,required=True)
    precio_total = fields.Float(String="Cantidad total",readonly=True,compute="Calc_total")

    @api.constrains('cantidad_butacas')
    def Calc_total(self):
        self.ensure_one
        if self.cantidad_butacas>self.butaca.sala.butacas_libres:
            raise ValidationError("Error el precio tiene que ser mayor de 0")
        else: 
            self.butaca.sala.butacas_libres = self.butaca.sala.cantidad_butacas_totales - self.cantidad_butacas
            self.precio_total = self.cantidad_butacas * self.butaca.precio

        
    
    

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

    
