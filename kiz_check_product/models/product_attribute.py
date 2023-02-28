# -*- coding: utf-8 -*-

import datetime
from odoo import models, fields, api


class product_attribute_check(models.Model):
    _inherit = 'product.attribute'

    att_check = fields.Selection([
        ('no', '未確認'),
        ('yes', '確認済'),
    ], default='no',
        string="確認",
        tracking=True)

    def write(self, values):
        flg = self._origin.att_check
        if self._origin.att_check == 'no' and values.get("att_check") == 'yes':
            values['att_check'] = 'yes'
        else:
            values['att_check'] = 'no'
        res = super(product_attribute_check, self).write(values)
        return res
