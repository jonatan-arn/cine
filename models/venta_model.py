# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class venta_model(models.Model):
    _name = 'cine.venta_model'
    _description = 'Modelo de las ventas de entradas'


    
    
    id = fields.Integer(String="Id venta entrada",index=True,required=True)
    snack = fields.One2many("cine.venta_snack_model","venta",String=" snack",required=True)
    entrada = fields.One2many("cine.venta_entradas_model","venta",String=" snack",required=True)
    precio_total = fields.Float(String="Cantidad total",readonly=True)
    fecha = fields.Datetime(string="Fecha",default=lambda self: datetime.now(), required=True)
    active = fields.Boolean(readonly=True, default=True)
    
    

  


    def eliminaFacturas(self):
          historialFacturas = self.search([("active","=","True")])
          for rec in historialFacturas:
                rec.active = "False"  
                rec.unlink()
    
    def ocultarFacturas(self):
        historialFacturas = self.search([("active","=","True")])
        for factura in historialFacturas:
            factura.active=False
        return True

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

    
