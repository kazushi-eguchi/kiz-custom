# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class kiz_view_archive_attribute(models.Model):
#     _name = 'kiz_view_archive_attribute.kiz_view_archive_attribute'
#     _description = 'kiz_view_archive_attribute.kiz_view_archive_attribute'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
