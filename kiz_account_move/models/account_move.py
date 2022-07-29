# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kiz_account_move(models.Model):
    _inherit = 'account.move'

    default_rate = fields.Float("レート", default=1)
    jma_order_no = fields.Char("JMU注番")


