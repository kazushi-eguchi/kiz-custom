# -*- coding: utf-8 -*-
# from odoo import http


# class KizCheckReport(http.Controller):
#     @http.route('/kiz_check_report/kiz_check_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kiz_check_report/kiz_check_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kiz_check_report.listing', {
#             'root': '/kiz_check_report/kiz_check_report',
#             'objects': http.request.env['kiz_check_report.kiz_check_report'].search([]),
#         })

#     @http.route('/kiz_check_report/kiz_check_report/objects/<model("kiz_check_report.kiz_check_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kiz_check_report.object', {
#             'object': obj
#         })
