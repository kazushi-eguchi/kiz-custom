# Copyright (C) 2021 Picg

from odoo import _, api, fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"
    ship_id = fields.Many2one(
        "ships.ship",
        string="ship"
    )
    weight = fields.Integer(
        name="weight",
        help="Enter in Kg"
    )
