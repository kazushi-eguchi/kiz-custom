# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kiz_partner(models.Model):
    _inherit = "res.partner"

    code = fields.Char("Partner Code")
    kana = fields.Char("kana")
    alias_name = fields.Char("alias name")
    allocated_code = fields.Char(string="allocated code 1", help="Enter the code assigned by your business partner.")
    allocated_code2 = fields.Char(string="allocated code 2")
    supplier_code = fields.Char(string="supplier code")
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
