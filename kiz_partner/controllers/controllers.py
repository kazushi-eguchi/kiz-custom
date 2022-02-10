# -*- coding: utf-8 -*-
# from odoo import http


# class KizPartner(http.Controller):
#     @http.route('/kiz_partner/kiz_partner/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kiz_partner/kiz_partner/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kiz_partner.listing', {
#             'root': '/kiz_partner/kiz_partner',
#             'objects': http.request.env['kiz_partner.kiz_partner'].search([]),
#         })

#     @http.route('/kiz_partner/kiz_partner/objects/<model("kiz_partner.kiz_partner"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kiz_partner.object', {
#             'object': obj
#         })
