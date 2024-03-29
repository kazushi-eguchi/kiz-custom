# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kiz_account_move(models.Model):
    _inherit = 'account.move'

    default_rate = fields.Float("レート", default=1)
    jma_order_no = fields.Char("JMU注番")
    quick_update = fields.Boolean()

    def _toggle_quick_update(self):
        if self.quick_update:
            self.quick_update = False
        else:
            self.quick_update = True
