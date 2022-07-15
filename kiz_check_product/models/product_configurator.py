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
