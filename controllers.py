# -*- coding: utf-8 -*-
from openerp import http

# class La(http.Controller):
#     @http.route('/la/la/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/la/la/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('la.listing', {
#             'root': '/la/la',
#             'objects': http.request.env['la.la'].search([]),
#         })

#     @http.route('/la/la/objects/<model("la.la"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('la.object', {
#             'object': obj
#         })