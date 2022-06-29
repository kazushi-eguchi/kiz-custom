# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class kiz_material_input_person_ext(models.Model):
#     _name = 'kiz_material_input_person_ext.kiz_material_input_person_ext'
#     _description = 'kiz_material_input_person_ext.kiz_material_input_person_ext'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
