# -*- coding: utf-8 -*-
# from odoo import http


# class KizProductConfiguratorQty(http.Controller):
#     @http.route('/kiz_product_configurator_qty/kiz_product_configurator_qty/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kiz_product_configurator_qty/kiz_product_configurator_qty/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kiz_product_configurator_qty.listing', {
#             'root': '/kiz_product_configurator_qty/kiz_product_configurator_qty',
#             'objects': http.request.env['kiz_product_configurator_qty.kiz_product_configurator_qty'].search([]),
#         })

#     @http.route('/kiz_product_configurator_qty/kiz_product_configurator_qty/objects/<model("kiz_product_configurator_qty.kiz_product_configurator_qty"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kiz_product_configurator_qty.object', {
#             'object': obj
#         })
