# -*- coding: utf-8 -*-
from odoo import  models, fields

class Alumno ( models.Model ):
    _name = "centro.alumno"
    name = fields.Text( string="Nombre", required=True )
    ape1 = fields.Text( string="Primer Apellido", required=True )
    ape2 = fields.Text( string="Segundo Apellido" )
    naci = fields.Date( string="Fecha Nacimiento", required=True )
    ciclo = fields.Selection( [ ('dam', 'DAM'), ('daw', 'DAW'), ('asir','ASIR') ], string="Ciclo Formativo" )
    nota = fields.Float( string="Nota Media" )
    empresa = fields.Many2one( "centro.empresa", store=True, string="Empresa de prácticas" )
    tutor = fields.Many2one( "centro.tutor", string="Tutor de prácticas" )
    def _nota_media_text_(self):
        """ Devuelve el texto correspondiente a la nota media """
        if 5 <= self.nota <= 7 :
            return "Aprobado"
        if 7 < self.nota <= 9:
            return "Notable"
        if 9 < self.nota <= 10:
            return "Sobresaliente"
        else:
            return "Suspendido"