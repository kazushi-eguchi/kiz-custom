# -*- coding: utf-8 -*-
# from odoo import http


# class KizPurchaseCustom(http.Controller):
#     @http.route('/kiz_purchase_custom/kiz_purchase_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kiz_purchase_custom/kiz_purchase_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kiz_purchase_custom.listing', {
#             'root': '/kiz_purchase_custom/kiz_purchase_custom',
#             'objects': http.request.env['kiz_purchase_custom.kiz_purchase_custom'].search([]),
#         })

#     @http.route('/kiz_purchase_custom/kiz_purchase_custom/objects/<model("kiz_purchase_custom.kiz_purchase_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kiz_purchase_custom.object', {
#             'object': obj
#         })
