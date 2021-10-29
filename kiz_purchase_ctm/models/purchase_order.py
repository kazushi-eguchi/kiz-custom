# -*- coding: utf-8 -*-

from odoo import models, fields, api


class KizPurchaseAdd(models.Model):
    _inherit = 'purchase.order.line'
    # _name = 'kiz_purchase_add.kiz_purchase_add'
    # _description = 'kiz_purchase_addon'

    purchase_line_image = fields.Binary(string="image")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
