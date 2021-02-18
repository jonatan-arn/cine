# -*- coding: utf-8 -*-

from odoo import models, fields, api


class salas_model(models.Model):
    _name = 'cine.salas_model'
    _description = 'Modelo de las salas'

    name = fields.Integer(String="Nº de sala",index=True,required=True)
    cantidad_butacas_totales = fields.Integer(String="Cantidad de butacas totales de la sala",index=True,required=True)
    #butacas_libres = fields.Integer(String="Butacas libres de la sala",index=True,required=True,default=lambda self: self.cantidad_butacas_totales)
    #butacas_libres = fields.Integer(String="Butacas libres de la sala",index=True,required=True)
    es3d = fields.Boolean(String="Es 3d",index=True,required=True)
    horario = fields.One2many("cine.horario_sala_model","sala")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100