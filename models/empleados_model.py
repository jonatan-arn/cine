# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class empleados_model(models.Model):
    _name = 'cine.empleados_model'
    _description = 'Modelo de los empleados'

    _sql_constraints = [('sql_constraints_id', 'unique(id)', 'Ese id ya existe'),
    ('sql_constraints_dni', 'unique(dni)', 'Ese dni ya existe')]
    id = fields.Integer(String="Id del trabajador",index=True,required=True)
    name = fields.Char(String="Nombre",index=True,required=True)
    dni = fields.Char(String="Dni",index=True,required=True)
    puesto_trabajo = fields.Char(String="Puesto de trabajo",required=True)



    @api.constrains('dni')
    def validate_dni(self):
        if not self.comprovar_dni():
            raise ValidationError("Error al introducir el dni")
  
    def comprovar_dni(self):
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        numeros = "1234567890"
        if (len(self.dni) == 9):
            letraControl = self.dni[8].upper()
            dni = self.dni[:8]
            if ( len(self.dni) == len( [n for n in dni if n in numeros] ) ):
                if tabla[int(dni)%23] == letraControl:
                    return True
        return False               
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
