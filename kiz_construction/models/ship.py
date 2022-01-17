# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kiz_construction_ship(models.Model):
    _inherit = "ships.ship"

    construction_ids = fields.One2many(
        'kiz_construction.kiz_construction',
        's_no'
    )
