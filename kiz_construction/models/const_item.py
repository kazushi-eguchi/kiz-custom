# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ConstItem(models.Model):
    _name = "const.item"
    _description = "Const item"
    _order = "id"

    name = fields.Char("ordered item")
