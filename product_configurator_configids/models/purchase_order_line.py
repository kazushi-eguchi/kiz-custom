# # -*- coding: utf-8 -*-
#
from odoo import models, fields, api

class KizPurchaseOrderLines(models.Model):
    _inherit = 'purchase.order.line'

    custom_values = fields.Char(compute="_compute_custom_values")

    def _compute_custom_values(self):
        for line in self:
            vals = []
            for custom_value in line.custom_value_ids:
                vals.append(custom_value.display_name + ": " + custom_value.value)
            line.custom_values = ",".join(vals)
