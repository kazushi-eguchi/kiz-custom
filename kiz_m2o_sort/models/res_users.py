# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kiz_construction_ship(models.Model):
    _inherit = "res.users"
    _order = "sequence"

    sequence = fields.Integer()
