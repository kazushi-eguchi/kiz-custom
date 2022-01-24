# -*- coding: utf-8 -*-
# from odoo import http


# class KizReport(http.Controller):
#     @http.route('/kiz_report/kiz_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kiz_report/kiz_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kiz_report.listing', {
#             'root': '/kiz_report/kiz_report',
#             'objects': http.request.env['kiz_report.kiz_report'].search([]),
#         })

#     @http.route('/kiz_report/kiz_report/objects/<model("kiz_report.kiz_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kiz_report.object', {
#             'object': obj
#         })
