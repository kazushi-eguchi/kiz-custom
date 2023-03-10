# -*- coding: utf-8 -*-
import logging
import datetime
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


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
        print(values)
        # _logger.debug('Create a %s with vals %s', self._name, values)
        if self._origin.check == 'no' and values.get("check") == 'yes':
            values['check'] = 'yes'
        else:
            if 'taxes_id' in values or 'image_1920' in values or 'sequence' in values:
                values['check'] = 'yes'
            else:
                values['check'] = 'no'
        res = super(product_configurator_check, self).write(values)
        return res
