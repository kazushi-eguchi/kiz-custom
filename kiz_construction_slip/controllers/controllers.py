# -*- coding: utf-8 -*-
# from odoo import http


# class KizConstructionSlip(http.Controller):
#     @http.route('/kiz_construction_slip/kiz_construction_slip/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kiz_construction_slip/kiz_construction_slip/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kiz_construction_slip.listing', {
#             'root': '/kiz_construction_slip/kiz_construction_slip',
#             'objects': http.request.env['kiz_construction_slip.kiz_construction_slip'].search([]),
#         })

#     @http.route('/kiz_construction_slip/kiz_construction_slip/objects/<model("kiz_construction_slip.kiz_construction_slip"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kiz_construction_slip.object', {
#             'object': obj
#         })
