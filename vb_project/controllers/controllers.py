# -*- coding: utf-8 -*-
from odoo import http

# class VbProject(http.Controller):
#     @http.route('/vb_project/vb_project/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vb_project/vb_project/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vb_project.listing', {
#             'root': '/vb_project/vb_project',
#             'objects': http.request.env['vb_project.vb_project'].search([]),
#         })

#     @http.route('/vb_project/vb_project/objects/<model("vb_project.vb_project"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vb_project.object', {
#             'object': obj
#         })