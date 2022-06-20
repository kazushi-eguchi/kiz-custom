# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ConstProduct(models.Model):
    _name = "const.product"
    _description = "Const product"
    _order = "id"

    name = fields.Char("product")
