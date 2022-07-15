# # -*- coding: utf-8 -*-
#
from odoo import models, fields, api


class ProductAttributeExt(models.Model):
    _inherit = 'product.attribute'
    _rec_name = 'name'

    display_name = fields.Char(string="表示名")
    product_name = fields.Char(string="表示名")
