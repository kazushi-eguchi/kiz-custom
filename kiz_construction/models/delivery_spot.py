# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ConstFiles(models.Model):
    _name = "purchase.delivery_spot"
    _description = "Delivery Spot"
    _order = "sequence"

    name = fields.Char("name")
    sequence = fields.Integer(default=1)
    # active = fields.Boolean()
