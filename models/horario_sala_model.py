# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class horario_sala_model(models.Model):
    _name = 'cine.horario_sala_model'
    _description = 'Modelo de los horario de las salas'

    name = fields.Char(compute="crearName")
    precio = fields.Integer(String="Precio de la pelicula",required=True)
    pelicula = fields.Many2one("cine.peliculas_model",String="Pelicula que se proyecta",index=True,required=True)
    hora = fields.Datetime(String="Hora a la que se proyecta la pelicula",required=True)
    sala = fields.Many2one("cine.salas_model",String="Sala donde se proyecta la pelicula",required=True)
    butacas_libres = fields.Integer(String="Butacas libres de la sala",required=True,default=lambda self: self.sala.cantidad_butacas_totales)
    
    
    @api.depends('name')
    def crearName(self):
        for r in self:
            hora =r.hora.strftime("%m/%d/%Y, %H:%M:%S")
            n_pelicula = "Pelicula: "+r.pelicula.name    
            n_sala = "Sala: "+r.sala.name
            r.name="Hora: ",str(hora),n_pelicula,n_sala

    @api.constrains('precio')
    def validate_precio(self):
        if (self.precio<=0):
            raise ValidationError("Error el precio tiene que ser mayor de 0")
    
    @api.constrains('butacas_libres')
    def validate_butacas(self):
        if (self.sala.cantidad_butacas_totales != self.butacas_libres):
            raise ValidationError("Error las butacas libres tienen que coincidir con las totales")

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
