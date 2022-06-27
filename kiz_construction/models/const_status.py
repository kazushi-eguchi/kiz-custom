# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kiz_construction_status(models.Model):
    _name = 'kiz_construction.status'
    _description = 'kiz_construction.status'
    _rec_name = "name"

    name = fields.Char("name")
    active = fields.Boolean("active")
    default = fields.Boolean()
    done = fields.Boolean()
