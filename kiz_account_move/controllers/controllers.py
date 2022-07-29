# -*- coding: utf-8 -*-
# from odoo import http


# class KizAccountMove(http.Controller):
#     @http.route('/kiz_account_move/kiz_account_move/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kiz_account_move/kiz_account_move/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kiz_account_move.listing', {
#             'root': '/kiz_account_move/kiz_account_move',
#             'objects': http.request.env['kiz_account_move.kiz_account_move'].search([]),
#         })

#     @http.route('/kiz_account_move/kiz_account_move/objects/<model("kiz_account_move.kiz_account_move"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kiz_account_move.object', {
#             'object': obj
#         })
