# -*- coding: utf-8 -*-
# from odoo import http


# class KizProductionManagementSlip(http.Controller):
#     @http.route('/kiz_production_management_slip/kiz_production_management_slip/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kiz_production_management_slip/kiz_production_management_slip/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kiz_production_management_slip.listing', {
#             'root': '/kiz_production_management_slip/kiz_production_management_slip',
#             'objects': http.request.env['kiz_production_management_slip.kiz_production_management_slip'].search([]),
#         })

#     @http.route('/kiz_production_management_slip/kiz_production_management_slip/objects/<model("kiz_production_management_slip.kiz_production_management_slip"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kiz_production_management_slip.object', {
#             'object': obj
#         })
