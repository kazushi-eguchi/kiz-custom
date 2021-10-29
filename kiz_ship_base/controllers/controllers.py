# -*- coding: utf-8 -*-
# from odoo import http


# class KizShipBase(http.Controller):
#     @http.route('/kiz_ship_base/kiz_ship_base/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kiz_ship_base/kiz_ship_base/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kiz_ship_base.listing', {
#             'root': '/kiz_ship_base/kiz_ship_base',
#             'objects': http.request.env['kiz_ship_base.kiz_ship_base'].search([]),
#         })

#     @http.route('/kiz_ship_base/kiz_ship_base/objects/<model("kiz_ship_base.kiz_ship_base"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kiz_ship_base.object', {
#             'object': obj
#         })
