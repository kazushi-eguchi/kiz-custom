# # -*- coding: utf-8 -*-
#
from odoo import models, fields, api


#
#


class KizPurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    _order = "production_management_ticket_period"

    #
    construction_id = fields.Many2one(
        comodel_name="kiz_construction.kiz_construction", string="construction"
    )
    account_id = fields.Many2one(
        comodel_name="account.analytic.account", string="production management slip no"
        , related='construction_id.no'
    )
    s_no = fields.Many2one(
        comodel_name="ships.ship",
        string="ship",
        related='construction_id.s_no'
    )  # S番
    deadline = fields.Date(string="deadline",
                           related='construction_id.deadline')  # 工事伝票納期
    drawing_number = fields.Char(string="drawing_number",
                           related='construction_id.drawing_number')  # 図面番号
    building = fields.Char(string="building",
                           related='construction_id.building')  # 建造所
    shipyard_full = fields.Char(string="造船所",
                           related='construction_id.shipyard_full')  # 建造所
    product_name = fields.Char(string="製作名称", related='construction_id.production_name')
    trading_company = fields.Many2one(
        comodel_name='res.partner', string='trading_company',
        related='construction_id.trading_company'
    )  # 商社
    shipyard_full = fields.Char(string="Shipyard Full", related='construction_id.shipyard_full')
    material_input_person = fields.Many2one('res.users',
                                            string="資材担当者",
                                            default=lambda self: self.env.user,
                                            domain=[("material_input_person_flg", "=", True)])
    production_management_ticket_period = fields.Date(string="制作管理票納期",
                                                      related='construction_id.production_management_ticket_period', store=True)  # 制作管理票納期
    order_qty = fields.Integer(compute="_get_order_qty_count", string="発注数量")
    order_received_qty = fields.Integer(compute="_get_order_received_qty_count", string="完了数量")
    not_complete = fields.Boolean(compute="_check_complete", search='_value_search', string="未入荷あり")

    def _value_search(self, operator, value):
        recs = self.search([]).filtered(lambda x: x.not_complete is True)
        if recs:
            return [('id', 'in', [x.id for x in recs])]

    def _check_complete(self):
        for rec in self:
            flg = rec.order_qty - rec.order_received_qty
            if flg == 0:
                rec.not_complete = False
            else:
                rec.not_complete = True

    def _get_order_qty_count(self):
        for rec in self:
            qty = 0
            for l in rec.order_line:
                qty += l.product_qty
            rec.order_qty = qty

    def _get_order_received_qty_count(self):
        for rec in self:
            qty = 0
            for l in rec.order_line:
                qty += l.qty_received
            rec.order_received_qty = qty


    # def clear(self):
    #     for rec in self:
    #         # rec.write({'partner_id': [(5, 0, 0)]})
    #         rec.partner_id = False

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
