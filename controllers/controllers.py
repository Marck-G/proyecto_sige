# -*- coding: utf-8 -*-
from odoo import http

# class Proyecyo(http.Controller):
#     @http.route('/proyecyo/proyecyo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proyecyo/proyecyo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('proyecyo.listing', {
#             'root': '/proyecyo/proyecyo',
#             'objects': http.request.env['proyecyo.proyecyo'].search([]),
#         })

#     @http.route('/proyecyo/proyecyo/objects/<model("proyecyo.proyecyo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proyecyo.object', {
#             'object': obj
#         })