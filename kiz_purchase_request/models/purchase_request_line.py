# -*- coding: utf-8 -*-

from odoo import models, fields, api


class KizPurchaseRequest(models.Model):
    _inherit = "purchase.request.line"
    request_img = fields.Binary(string="image")
#     _description = 'kiz_purchase_request.kiz_purchase_request'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
