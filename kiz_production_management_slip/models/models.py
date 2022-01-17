# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kiz_production_management_slip(models.Model):
     _name = 'kiz_production_management_slip.kiz_production_management_slip'
     _description = 'kiz_production_management_slip.kiz_production_management_slip'

     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
