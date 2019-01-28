# -*- coding: utf-8 -*-

from odoo import models, fields, api

class centro_empresa( models.Model ):
    _name   = 'centro.empresa'
    name    = fields.Text(string="Nombre", required=True)
    direccion = fields.Text()
    alumnos = fields.One2many('centro.alumno')

class centro_alumno( models.Model ):
    _name = "centro.alumno"
    name = fields.Text( string="Nombre", required=True )
    ape1 = fields.Text( string="Primer Apellido", required=True )
    ape2 = fields.Text( string="Segundo Apellido" )
    naci = fields.Date( string="Fecha Nacimiento", required=True )
    ciclo = fields.Selection( [ ('dam', 'DAM'), ('daw', 'DAW'), ('asir','ASIR') ], string="Ciclo Formativo" );
    nota = fields.Float( string="Nota Media" )
    def _nota_media_text_(self, _nota):
        """ Devuelve el texto correspondiente a la nota media """
        if 5 <= _nota <= 7 :
            return "Aprobado"
        if 7 < _nota <= 9:
            return "Notable"
        if 9 < _nota <= 10:
            return "Sobresaliente"
        else:
            return "Suspendido"

# class proyecyo(models.Model):
#     _name = 'proyecyo.proyecyo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100