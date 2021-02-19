# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime
class venta_snack_model(models.Model):
    _name = 'cine.venta_snack_model'
    _description = 'Modelo de las ventas de entradas'


    _sql_constraints = [('sql_constraints_id', 'unique(id)', 'Ese id ya existe')]
    
    id = fields.Integer(String="Id venta entrada",index=True,required=True)
    cantidad_snack= fields.Integer(String="Cantidad de butacas totales de la sala",index=True,required=True)
    snack = fields.Many2one("cine.snacks_model",String="Precio del snack",index=True,required=True)
    precio_total = fields.Float(String="Cantidad total",readonly=True,compute="Calc_total")
    fecha = fields.Datetime(string="Fecha",default=lambda self: datetime.now(), required=True)
    active = fields.Boolean(readonly=True, default=True)

    @api.depends('cantidad_snack')
    def Calc_total(self):            
        for r in self:
            r.precio_total = r.cantidad_snack * r.snack.precio
            
            
    def eliminaFacturas(self):
          historialFacturas = self.search([("active","=","True")])
          for rec in historialFacturas:
                rec.active = "False"  
                rec.unlink()
    

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

    
