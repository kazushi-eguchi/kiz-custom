# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kiz_users(models.Model):
    _inherit = 'res.users'

    test = fields.Char()
    material_input_person_flg = fields.Boolean()
