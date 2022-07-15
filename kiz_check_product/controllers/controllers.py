# -*- coding: utf-8 -*-
# from odoo import http


# class KizCheckProduct(http.Controller):
#     @http.route('/kiz_check_product/kiz_check_product/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kiz_check_product/kiz_check_product/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kiz_check_product.listing', {
#             'root': '/kiz_check_product/kiz_check_product',
#             'objects': http.request.env['kiz_check_product.kiz_check_product'].search([]),
#         })

#     @http.route('/kiz_check_product/kiz_check_product/objects/<model("kiz_check_product.kiz_check_product"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kiz_check_product.object', {
#             'object': obj
#         })
