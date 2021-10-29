# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kiz_construction(models.Model):
     _name = 'kiz_construction.kiz_construction'
     _description = 'kiz_construction.kiz_construction'

     no = fields.Char(string="construction no", require=True, Transrate=True)
     status = fields.Selection([
          ('lead','lead'),
          ('promising','Promising'),
          ('contract','contract'),
     ],required= True, default='lead')
     deadline = fields.Date(string="deadline")
     account_executive =fields.Char(string="account executive")
     trading_company = fields.Many2one('res.company', string='Company', required=True)
     trading_company_short_name =fields.Char(string="trading company short name")
     branch = fields.Char(string="Branch")
     shipyard_full = fields.Char(string="Shipyard Full")
     shipyard_short = fields.Char(string="Shipyard short")
     building = fields.Char(string="building")
     s_no = fields.Char(string="S No.")
     name = fields.Char(string="name")
     first_category = fields.Char(string="First category")
     second_category = fields.Char(string="Second category")
     ship_class =fields.Char(string="Ship class")
     drawing_number = fields.Char(string="drawing number")
     painting = fields.Char(string="painting")
     product_number = fields.Char(string="product number")
     date_of_issue = fields.Date(string="date of issue")
     designer = fields.Char(string="Designer")
     machining_drawing = fields.Char(string="Machining drawing")
     in_house_construction_drawing = fields.Char(string="In-house construction drawing")
     attachment_id = fields.Many2one('ir.attachment', string="Attachment")
     isomorphism = fields.Char(string="Isomorphism")
     items = fields.Char(string="items")
     note = fields.Text(string="note")
     design_note = fields.Char(string="Design note")
     material_input_person = fields.Char(string="Material input person")
     production_place = fields.Char(string="Production place")
     china_arrival_date = fields.Date(string="China arrival date")
     procurement_date = fields.Date(string="Procurement date")
     departure_date = fields.Date(string="Departure date")
     in_days =fields.Integer(string="in days")
     in_date = fields.Date(string="in date")
     china_days =fields.Integer(string="china days")
     china_date = fields.Date(string="china date")
     consultation_drawing = fields.Many2one('ir.attachment', string="Consultation drawing")
     approved_drawing = fields.Many2one('ir.attachment', string="Approved drawing")
     construction_drawing = fields.Many2one('ir.attachment', string="Construction drawing")
     steel_material_order_date = fields.Date(string="Steel material order date")
     steel_material_arrangement_date =fields.Date(string="Steel material arrangement date")
     paint_order_date = fields.Date(string="paint order date")
     paint_arrangement_date = fields.Date(string="paint arrangement date")
     gross_weight = fields.Float(string="Gross weight")
     expected_gross_weight = fields.Float(string="Expected gross weight")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
