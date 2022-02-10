# Copyright (C) 2021 Picg

from odoo import api, fields, models


class ShipsType(models.Model):
    _name = "ships.type"
    _description = "ship type"
    # _rec_name = "combination"
    name = fields.Char("name")
