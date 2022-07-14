# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ConstFiles(models.Model):
    _name = "purchase.delivery_spot"
    _description = "Delivery Spot"
    _order = "name"

    name = fields.Char("name")
    # active = fields.Boolean()
