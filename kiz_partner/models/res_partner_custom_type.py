# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kiz_partner_custom_type(models.Model):
    _name = "res.partner.custom_type"
    _description = "type"
    _rec_name = "name"

    name = fields.Char(string="name")
