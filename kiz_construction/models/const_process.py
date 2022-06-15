# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ConstProcess(models.Model):
    _name = "const.process"
    _description = "Const process"
    _order = "id"

    name = fields.Char("process name")
