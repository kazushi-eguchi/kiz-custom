# -*- coding: utf-8 -*-
# from odoo import http


# class KizProjectCtm(http.Controller):
#     @http.route('/kiz_project_ctm/kiz_project_ctm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kiz_project_ctm/kiz_project_ctm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kiz_project_ctm.listing', {
#             'root': '/kiz_project_ctm/kiz_project_ctm',
#             'objects': http.request.env['kiz_project_ctm.kiz_project_ctm'].search([]),
#         })

#     @http.route('/kiz_project_ctm/kiz_project_ctm/objects/<model("kiz_project_ctm.kiz_project_ctm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kiz_project_ctm.object', {
#             'object': obj
#         })
