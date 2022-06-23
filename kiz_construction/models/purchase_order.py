# # -*- coding: utf-8 -*-
#
from odoo import models, fields, api


#
#


class KizPurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    #
    construction_id = fields.Many2one(
        comodel_name="kiz_construction.kiz_construction", string="construction"
    )
    account_id = fields.Many2one(
        comodel_name="account.analytic.account", string="production management slip no"
    )
    s_no = fields.Many2one(
        comodel_name="ships.ship",
        string="ship"
    )  # S番
    deadline = fields.Date(string="deadline",
                           related='construction_id.deadline')  # 工事伝票納期
    drawing_number = fields.Char(string="drawing_number",
                           related='construction_id.drawing_number')  # 図面番号
    building = fields.Char(string="building",
                           related='construction_id.building')  # 建造所
    product_name = fields.Char(string="製作名称", related='construction_id.production_name')
    trading_company = fields.Many2one(
        comodel_name='res.partner', string='trading_company')  # 商社
    shipyard_full = fields.Char(string="Shipyard Full")
    material_input_person = fields.Char(related='construction_id.material_input_person.name', string="資材担当者")
    production_management_ticket_period = fields.Date(string="制作管理票納期",
                           related='construction_id.production_management_ticket_period')  # 制作管理票納期
    # def _compute_account_id(self):
    #
    #     a = self.env["purchase.order.line"].search_read([], [])
    #     #b = self.purchase_lines
    #     print(self.id)
    #     print(a)
    #     self.account_id = self.env["purchase.order.line"].search([("order_id", "=", self.id)]).account_analytic_id
    #     print(self.account_id)

    # @api.depends("account_id")
    # def _compute_account_id(self):
    #     a = self.env["kiz_construction.kiz_construction"].search_read([], [])
    # #     # b = self.purchase_lines
    #     print(self.id)
    #     print(a)
    #     self.account_id = self.env["purchase.order.line"].search([("order_id", "=", self.id)]).account_analytic_id
    #     print(self.account_id)
