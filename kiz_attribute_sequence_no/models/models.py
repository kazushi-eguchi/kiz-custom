# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class kiz_attribute_sequence_no(models.Model):
#     _name = 'kiz_attribute_sequence_no.kiz_attribute_sequence_no'
#     _description = 'kiz_attribute_sequence_no.kiz_attribute_sequence_no'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
