# -*- coding: utf-8 -*-
# from odoo import http


# class KizPoLineCheck(http.Controller):
#     @http.route('/kiz_po_line_check/kiz_po_line_check/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kiz_po_line_check/kiz_po_line_check/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kiz_po_line_check.listing', {
#             'root': '/kiz_po_line_check/kiz_po_line_check',
#             'objects': http.request.env['kiz_po_line_check.kiz_po_line_check'].search([]),
#         })

#     @http.route('/kiz_po_line_check/kiz_po_line_check/objects/<model("kiz_po_line_check.kiz_po_line_check"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kiz_po_line_check.object', {
#             'object': obj
#         })
