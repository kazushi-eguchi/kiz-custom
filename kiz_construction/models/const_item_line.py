# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ConstItemLine(models.Model):
    _name = "const.item_line"
    _description = "Const item line"
    _order = "id"

    name = fields.Many2one("const.item", string="ordered item")  # 品名
    supplier = fields.Many2one("res.partner", string="supplier")  # 手配先
    request_date = fields.Date("request_date")  # 手配日
    const_id = fields.Many2one("kiz_construction.kiz_construction", string="construction")
