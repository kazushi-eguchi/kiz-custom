# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kiz_purchase_order_line_account(models.Model):
    _inherit = 'purchase.order.line'

    invoice_deliver_date = fields.Date(string="請求書納品日", default=lambda self: self.date_planned)
