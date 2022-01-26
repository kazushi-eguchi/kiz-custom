# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kiz_construction_ship(models.Model):
    _inherit = "res.partner"
    production_control_ids = fields.One2many(
        'kiz_construction.kiz_construction',
        'trading_company'
    )
