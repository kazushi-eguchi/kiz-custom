# # -*- coding: utf-8 -*-
#
from odoo import models, fields, api

class KizPurchaseOrderLines(models.Model):
    _inherit = 'purchase.order.line'

    # custom_values = fields.Text(
    #     string="custom_values",
    #     comodel_name="product.config.session.custom.value",
    #     readonly=True,
    #     related="config_session_id.value",
    #     store=True,
    # )