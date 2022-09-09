# -*- coding: utf-8 -*-
# from odoo import http


# class KizCustomReport(http.Controller):
#     @http.route('/kiz_custom_report/kiz_custom_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kiz_custom_report/kiz_custom_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kiz_custom_report.listing', {
#             'root': '/kiz_custom_report/kiz_custom_report',
#             'objects': http.request.env['kiz_custom_report.kiz_custom_report'].search([]),
#         })

#     @http.route('/kiz_custom_report/kiz_custom_report/objects/<model("kiz_custom_report.kiz_custom_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kiz_custom_report.object', {
#             'object': obj
#         })
