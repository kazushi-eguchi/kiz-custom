# -*- coding: utf-8 -*-
# from odoo import http


# class ConfigProductCategoryMenu(http.Controller):
#     @http.route('/config_product_category_menu/config_product_category_menu/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/config_product_category_menu/config_product_category_menu/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('config_product_category_menu.listing', {
#             'root': '/config_product_category_menu/config_product_category_menu',
#             'objects': http.request.env['config_product_category_menu.config_product_category_menu'].search([]),
#         })

#     @http.route('/config_product_category_menu/config_product_category_menu/objects/<model("config_product_category_menu.config_product_category_menu"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('config_product_category_menu.object', {
#             'object': obj
#         })
