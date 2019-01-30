# -*- coding: utf-8 -*-
from odoo import models, fields
class Tutor (models.Model):
    _name = "centro.tutor"
    name = fields.Text( string="Nombre" )
    # un tutor se encarga de n alumnos
    alumnos = fields.One2many( 'centro.alumno', inverse_name='tutor' )
