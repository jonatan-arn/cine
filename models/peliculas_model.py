# -*- coding: utf-8 -*-

from odoo import models, fields, api


class peliculas_model(models.Model):
    _name = 'cine.peliculas_model'
    _description = 'Modelo de la pelicula'

    name = fields.Char(String="Nombre",index=True,required=True)
    director = fields.Char(String="Director",required=True)
    protagonista = fields.Char(String="Protagonista",required=True)
    pegi = fields.Selection(string="Pegi", default='todas las edades', selection=[('todas las edades','todas las edades'),('+7', '+7'),('+12', '+12'),('+13', '+13'),('+14', '+14'),('+16', '+16'),('+18', '+18')], required=True)
    fecha_estreno = fields.Date(String="Fecha de estreno",required=True)
    fecha_fin_en_el_cine = fields.Date(String="Fecha de salida en el cine",required=True)
    poster = fields.Binary(String="Poster")
    horario = fields.One2many("cine.horario_sala_model","pelicula")

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
