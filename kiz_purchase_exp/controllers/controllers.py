# -*- coding: utf-8 -*-
# from odoo import http


# class KizPurchaseExp(http.Controller):
#     @http.route('/kiz_purchase_exp/kiz_purchase_exp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kiz_purchase_exp/kiz_purchase_exp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kiz_purchase_exp.listing', {
#             'root': '/kiz_purchase_exp/kiz_purchase_exp',
#             'objects': http.request.env['kiz_purchase_exp.kiz_purchase_exp'].search([]),
#         })

#     @http.route('/kiz_purchase_exp/kiz_purchase_exp/objects/<model("kiz_purchase_exp.kiz_purchase_exp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kiz_purchase_exp.object', {
#             'object': obj
#         })
