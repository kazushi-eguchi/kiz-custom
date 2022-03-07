# -*- coding: utf-8 -*-

from odoo import models, fields, api


class KizPurchaseRequest(models.Model):
    _inherit = "purchase.request"
    account_id = fields.Many2one(
        comodel_name="account.analytic.account", string="production management slip no"
    )
    # s_no = fields.Many2one(comdel_name="ships.ship", compute='_compute_sno')
    # s_no = fields.Char(compute='_compute_sno')
#     _description = 'kiz_purchase_request.kiz_purchase_request'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

    @api.model
    def _prepare_purchase_order(self):
        data = super()._prepare_purchase_order()
        data['account_id'] = self.account_id
        print("test")
        return data

    # @api.onchange("account_id")
    # def _compute_sno(self):
    #     self.ensure_one()
    #     #a = self.env["kiz_construction.kiz_construction"].search_read([], [])
    # # #     # b = self.purchase_lines
    #
    #     print(self.account_id)
    #     self.s_no = self.env["ships.ship"].search([("construction_ids", "=", self.account_id.name)]).sno
    #     print(self.env["kiz_construction.kiz_construction"].search([("no", "=", self.account_id.name)]).shipyard_full)
    #     print(self.s_no)
