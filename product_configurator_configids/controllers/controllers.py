# -*- coding: utf-8 -*-
# from odoo import http


# class ProductConfiguratorConfigids(http.Controller):
#     @http.route('/product_configurator_configids/product_configurator_configids/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_configurator_configids/product_configurator_configids/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_configurator_configids.listing', {
#             'root': '/product_configurator_configids/product_configurator_configids',
#             'objects': http.request.env['product_configurator_configids.product_configurator_configids'].search([]),
#         })

#     @http.route('/product_configurator_configids/product_configurator_configids/objects/<model("product_configurator_configids.product_configurator_configids"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_configurator_configids.object', {
#             'object': obj
#         })
