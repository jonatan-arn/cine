# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class horario_sala_model(models.Model):
    _name = 'cine.horario_sala_model'
    _description = 'Modelo de los horario de las salas'

    name = fields.Char(compute="crearName")
    precio = fields.Integer(String="Precio de la pelicula",index=True,required=True)
    pelicula = fields.Many2one("cine.peliculas_model",String="Pelicula que se proyecta",index=True,required=True)
    hora = fields.Datetime(String="Hora a la que se proyecta la pelicula",index=True,required=True)
    sala = fields.Many2one("cine.salas_model",String="Sala donde se proyecta la pelicula",required=True)
    venta = fields.One2many("cine.venta_entradas_model","butaca")

    def crearName(self):
        self.ensure_one
        hora =self.hora.strftime("%m/%d/%Y, %H:%M:%S")
        n_pelicula = "Pelicula: "+self.pelicula.name    
        n_sala = "Sala: "+str(self.sala.id)
        self.name="Hora: ",str(hora),n_pelicula,n_sala

    @api.constrains('precio')
    def validate_dni(self):
        if (self.precio<=0):
            raise ValidationError("Error el precio tiene que ser mayor de 0")

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
