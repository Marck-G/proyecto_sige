# -*- coding: utf-8 -*-

from odoo import models, fields

class Empresa ( models.Model ):
    _name = 'centro.empresa'
    name = fields.Text(string="Nombre", required=True)
    direccion = fields.Text()
    alumnos = fields.One2many('centro.alumno', inverse_name='empresa')