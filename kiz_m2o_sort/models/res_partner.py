# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kiz_partner(models.Model):
    _inherit = "res.partner"
    _order = "sequence"

    sequence = fields.Integer()
