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

    product_name = fields.Char(string="name")
    trading_company = fields.Many2one(
        comodel_name='res.partner', string='trading_company')  # 商社
    shipyard_full = fields.Char(string="Shipyard Full")

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
