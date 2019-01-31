# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Empresa ( models.Model ):
    _name = 'empresa.empresa'
    name = fields.Char(string="Nombre", required=True)
    direccion = fields.Char()
    alumnos = fields.One2many('centro.alumno', inverse_name='empresa')

class Alumno ( models.Model ):
    _name = "centro.alumno"
    name = fields.Char( string="Nombre", required=True )
    ape1 = fields.Char( string="Primer Apellido", required=True )
    ape2 = fields.Char( string="Segundo Apellido" )
    naci = fields.Date( string="Fecha Nacimiento", required=True )
    ciclo = fields.Selection( [ ('dam', 'DAM'), ('daw', 'DAW'), ('asir','ASIR') ], string="Ciclo Formativo" )
    nota = fields.Float( string="Nota Media" )
    empresa = fields.Many2one( "empresa.empresa", store=True, string="Empresa de prácticas" )
    tutor = fields.Many2one( "centro.tutor", string="Tutor de prácticas" )
    @api.one
    def _nota_media_text_(self):
        """ Devuelve el texto correspondiente a la nota media """
        if 5 <= self.nota <= 7 :
            self.text = "Aprobado"
        elif 7 < self.nota <= 9:
            self.text =  "Notable"
        elif 9 < self.nota <= 10:
            self.text =  "Sobresaliente"
        else:
            self.text = "Suspendido"

    text = fields.Text( compute='_nota_media_text_', string="Nota Media" );

class Tutor (models.Model):
    _name = "centro.tutor"
    name = fields.Char( string="Nombre" )
    # un tutor se encarga de n alumnos
    alumnos = fields.One2many( 'centro.alumno', inverse_name='tutor' )