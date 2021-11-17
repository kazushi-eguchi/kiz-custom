# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class CrmLead(models.Model):
    _inherit = "project.project"
    ship_id = fields.Many2one(
        "ships.ship",
        string="ship"
    )
    weight = fields.Integer(
        name="weight",
        help="Enter in Kg"
    )
    manage_no = fields.Char("Manage No", required=True)
