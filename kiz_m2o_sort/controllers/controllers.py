# -*- coding: utf-8 -*-
# from odoo import http


# class KizM2oSort(http.Controller):
#     @http.route('/kiz_m2o_sort/kiz_m2o_sort/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kiz_m2o_sort/kiz_m2o_sort/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kiz_m2o_sort.listing', {
#             'root': '/kiz_m2o_sort/kiz_m2o_sort',
#             'objects': http.request.env['kiz_m2o_sort.kiz_m2o_sort'].search([]),
#         })

#     @http.route('/kiz_m2o_sort/kiz_m2o_sort/objects/<model("kiz_m2o_sort.kiz_m2o_sort"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kiz_m2o_sort.object', {
#             'object': obj
#         })
