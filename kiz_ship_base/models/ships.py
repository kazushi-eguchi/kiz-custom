# Copyright (C) 2021 Picg

from odoo import api, fields, models

class ShipsShip(models.Model):
    _name = "ships.ship"
    _description = "ship"
    _rec_name = "combination"
    name = fields.Char("ship", required=True)
    sno = fields.Char("sno")
    note = fields.Text(string="Description")
    ship_image = fields.Binary(string="Ship Image")
    ship_class = fields.Char(string="Ship Class")
    total_weight = fields.Float(string="Total weight")
    ship_ids = fields.One2many(
        comodel_name="crm.lead",
        inverse_name="ship_id",
        string="lead",
    )
    ship_owner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Ship owner",
        required=False,
        ondelete="set null",
    )
    client_id = fields.Many2one(
        comodel_name="res.partner",
        string="Client Name",
        required=False,
        ondelete="set null",
    )
    client_construction_site = fields.Char(string="Construction site")
    publication_start_date = fields.Date(string="Publication start date")
    launch_date = fields.Date(string="Launch date")
    delivery_date = fields.Date(string="Delivery date")
    lead_count = fields.Integer(string="Lead Count", compute="_compute_lead_count")

    combination = fields.Char(string='Combination', compute='_compute_fields_combination')

    @api.depends('sno', 'name')
    def _compute_fields_combination(self):
        for ship in self:
            if ship.sno == False:
                ship.combination = ship.name
            else:
                ship.combination = ship.sno + ' ' + ship.name

    def _compute_lead_count(self):
        for rec in self:
            lead_count = self.env['crm.lead'].search_count([('ship_id', '=', rec.id)])
            rec.lead_count = lead_count

    def action_open_lead(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Leads',
            'res_model': 'crm.lead',
            'domain': [('ship_id', '=', self.id)],
            'view_mode': 'tree,form',
            'target': 'current',
            'context': {
                'default_ship_id': self.id,
            }
        }

    def create_lead(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'crm.lead',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_ship_id': self.id,
            }
        }