# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ConstProductLine(models.Model):
    _name = "const.product_line"
    _description = "Const product line"
    _order = "id"

    name = fields.Many2one("const.product", string="product")  # 製品
    qty = fields.Integer()  # 個数
    uom = fields.Char()  # 個数
    place = fields.Char()  # 制作場所
    note = fields.Char()  #
    const_id = fields.Many2one("kiz_construction.kiz_construction", string="construction")
