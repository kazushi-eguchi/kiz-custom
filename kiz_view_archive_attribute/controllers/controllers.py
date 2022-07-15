# -*- coding: utf-8 -*-
# from odoo import http


# class KizViewArchiveAttribute(http.Controller):
#     @http.route('/kiz_view_archive_attribute/kiz_view_archive_attribute/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kiz_view_archive_attribute/kiz_view_archive_attribute/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kiz_view_archive_attribute.listing', {
#             'root': '/kiz_view_archive_attribute/kiz_view_archive_attribute',
#             'objects': http.request.env['kiz_view_archive_attribute.kiz_view_archive_attribute'].search([]),
#         })

#     @http.route('/kiz_view_archive_attribute/kiz_view_archive_attribute/objects/<model("kiz_view_archive_attribute.kiz_view_archive_attribute"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kiz_view_archive_attribute.object', {
#             'object': obj
#         })
