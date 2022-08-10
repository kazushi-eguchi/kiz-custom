# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta, datetime, date


class kiz_purchase_order_quick_update(models.Model):
    _inherit = 'purchase.order'

    quick_update = fields.Boolean()

    def toggle_quick_update(self):
        if self.quick_update:
            self.quick_update = False
        else:
            self.quick_update = True

    def copy(self, default=None):
        """Change date_planned for lines without product after calling super"""
        default = dict(default or {})
        default["date_order"] = datetime.now()
        default["partner_id"] = self.env['res.partner'].search([('name', 'ilike', '申請')], limit=1).id
        new_po = super().copy(default=default)
        for line in new_po.order_line:
            line.invoice_deliver_date = False

        return new_po