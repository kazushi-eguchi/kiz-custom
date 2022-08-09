# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kiz_purchase_order_quick_update(models.Model):
    _inherit = 'purchase.order'

    quick_update = fields.Boolean()

    def toggle_quick_update(self):
        if self.quick_update:
            self.quick_update = False
        else:
            self.quick_update = True
