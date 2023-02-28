# -*- coding: utf-8 -*-

import datetime
from odoo import models, fields, api


class product_configurator_check(models.Model):
    _inherit = 'product.template'

    check = fields.Selection([
        ('no', '未確認'),
        ('yes', '確認済'),
    ], default='no',
        string="確認",
        tracking=True)

    def write(self, values):
        flg = self._origin.check
        if self._origin.check == 'no' and values.get("check") == 'yes':
            values['check'] = 'yes'
        else:
            values['check'] = 'no'
        res = super(product_configurator_check, self).write(values)
        return res
