# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ConstProcessLine(models.Model):
    _name = "const.process_line"
    _description = "Const process line"
    _order = "id"

    name = fields.Many2one("const.process", string="process name")  # 工程
    request_date = fields.Date("request_date")  # 依頼日
    dead_line = fields.Date("dead_line")  # 納期
    const_id = fields.Many2one("kiz_construction.kiz_construction", string="construction")
