# -*- coding: utf-8 -*-
# from odoo import http


# class KizMaterialInputPersonExt(http.Controller):
#     @http.route('/kiz_material_input_person_ext/kiz_material_input_person_ext/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kiz_material_input_person_ext/kiz_material_input_person_ext/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kiz_material_input_person_ext.listing', {
#             'root': '/kiz_material_input_person_ext/kiz_material_input_person_ext',
#             'objects': http.request.env['kiz_material_input_person_ext.kiz_material_input_person_ext'].search([]),
#         })

#     @http.route('/kiz_material_input_person_ext/kiz_material_input_person_ext/objects/<model("kiz_material_input_person_ext.kiz_material_input_person_ext"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kiz_material_input_person_ext.object', {
#             'object': obj
#         })
