# -*- coding: utf-8 -*-
# from odoo import http


# class KizAttributeSequenceNo(http.Controller):
#     @http.route('/kiz_attribute_sequence_no/kiz_attribute_sequence_no/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kiz_attribute_sequence_no/kiz_attribute_sequence_no/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kiz_attribute_sequence_no.listing', {
#             'root': '/kiz_attribute_sequence_no/kiz_attribute_sequence_no',
#             'objects': http.request.env['kiz_attribute_sequence_no.kiz_attribute_sequence_no'].search([]),
#         })

#     @http.route('/kiz_attribute_sequence_no/kiz_attribute_sequence_no/objects/<model("kiz_attribute_sequence_no.kiz_attribute_sequence_no"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kiz_attribute_sequence_no.object', {
#             'object': obj
#         })
