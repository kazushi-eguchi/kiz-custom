# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kiz_construction(models.Model):
    _name = 'kiz_construction.kiz_construction'
    _description = 'kiz_construction.kiz_construction'

    construction_slip_number = fields.Char(string="construction slip number", Transrate=True)  # 制作管理番号
    construction_slip_status = fields.Char(string="construction slip status")
    production_management_ticket_period = fields.Date(string="production management ticket period")  # 制作管理票納期
    no = fields.Many2one(
        comodel_name="account.analytic.account", string="production management slip no"
    )
    status = fields.Char(string="status")# 工事伝票ステータス
    deadline = fields.Date(string="deadline")  # 工事伝納期
    account_executive = fields.Char(string="account executive")  # 営業担当者
    trading_company = fields.Many2one('res.company', string='Company')  # 商社
    trading_company_short_name = fields.Char(string="trading company short name")  # 商社略称
    branch = fields.Char(string="Branch")  # 支社
    shipyard_full = fields.Char(string="Shipyard Full")
    shipyard_short = fields.Char(string="Shipyard short")
    building = fields.Char(string="building")
    s_no = fields.Many2one(
        "ships.ship",
        string="ship"
    )  # S番
    name = fields.Char(string="name")
    production_name = fields.Char(string="Production Name")
    first_category = fields.Char(string="First category")
    second_category = fields.Char(string="Second category")
    ship_class = fields.Char(string="Ship class")
    drawing_number = fields.Char(string="drawing number")
    painting = fields.Char(string="painting")
    product_number = fields.Char(string="product number")
    date_of_issue = fields.Date(string="date of issue")
    finished_making_the_day = fields.Date(string="Finished making the day")
    designer = fields.Char(string="Designer")
    machining_drawing = fields.Char(string="Machining drawing")
    in_house_construction_drawing = fields.Char(string="In-house construction drawing")
    attachment_id = fields.Many2one('ir.attachment', string="Attachment")
    isomorphism = fields.Char(string="Isomorphism")
    items = fields.Char(string="items")
    note = fields.Text(string="note")
    design_note = fields.Char(string="Design note")
    nesting_notes = fields.Char(string="Nesting Notes")
    material_input_person = fields.Char(string="Material input person")
    production_place = fields.Char(string="Production place")
    correction_area = fields.Char(string="correction area")
    china_arrival_date = fields.Date(string="China arrival date")
    procurement_date = fields.Date(string="Procurement date")
    departure_date = fields.Date(string="Departure date")
    in_days = fields.Integer(string="in days")
    in_date = fields.Date(string="in date")
    china_days = fields.Integer(string="china days")
    china_date = fields.Date(string="china date")
    consultation_drawing = fields.Many2one('ir.attachment', string="Consultation drawing")
    approved_drawing = fields.Many2one('ir.attachment', string="Approved drawing")
    construction_drawing = fields.Many2one('ir.attachment', string="Construction drawing")
    steel_material_order_date = fields.Date(string="Steel material order date")
    steel_material_arrangement_date = fields.Date(string="Steel material arrangement date")
    paint_order_date = fields.Date(string="paint order date")
    paint_arrangement_date = fields.Date(string="paint arrangement date")
    gross_weight = fields.Integer(string="Gross weight")
    expected_gross_weight = fields.Integer(string="Expected gross weight", related='s_no.total_weight')
    #分析勘定
    # analytic_account_id = fields.Many2one(
    #     comodel_name="account.analytic.account", string="Analytic Account"
    # )

    #     value = fields.Integer()
    #     value2 = fields.Float(compute="_value_pc", store=True)
    #     description = fields.Text()
    #
    #     @api.depends('value')
    #     def _value_pc(self):
    #         for record in self:
    #             record.value2 = float(record.value) / 100
    def create_pr(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'purchase.request',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_name': self.no.name,
                'default_account_id': self.no.id,
            }
        }
