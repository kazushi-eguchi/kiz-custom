# -*- coding: utf-8 -*-
# from odoo import http


# class KizConstruction(http.Controller):
#     @http.route('/kiz_construction/kiz_construction/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kiz_construction/kiz_construction/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kiz_construction.listing', {
#             'root': '/kiz_construction/kiz_construction',
#             'objects': http.request.env['kiz_construction.kiz_construction'].search([]),
#         })

#     @http.route('/kiz_construction/kiz_construction/objects/<model("kiz_construction.kiz_construction"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kiz_construction.object', {
#             'object': obj
#         })
