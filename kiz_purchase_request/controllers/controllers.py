# -*- coding: utf-8 -*-
# from odoo import http


# class KizPurchaseRequest(http.Controller):
#     @http.route('/kiz_purchase_request/kiz_purchase_request/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kiz_purchase_request/kiz_purchase_request/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kiz_purchase_request.listing', {
#             'root': '/kiz_purchase_request/kiz_purchase_request',
#             'objects': http.request.env['kiz_purchase_request.kiz_purchase_request'].search([]),
#         })

#     @http.route('/kiz_purchase_request/kiz_purchase_request/objects/<model("kiz_purchase_request.kiz_purchase_request"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kiz_purchase_request.object', {
#             'object': obj
#         })
