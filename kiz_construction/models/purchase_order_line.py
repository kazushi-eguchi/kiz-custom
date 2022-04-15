# -*- coding: utf-8 -*-

from odoo import models, fields, api


class KizPurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    #
    account_id = fields.Many2one(
        related='order_id.account_id',
        comodel_name="account.analytic.account", string="production management slip no"
    )
    s_no = fields.Many2one(
        related='order_id.s_no',
        comodel_name="ships.ship",
        string="ship"
    )  # S番

    product_name = fields.Char(
        related='order_id.product_name',
        string="name")
    trading_company = fields.Many2one(
        related='order_id.trading_company',
        comodel_name='res.partner', string='trading_company')  # 商社
    shipyard_full = fields.Char(
        related='order_id.shipyard_full',
        string="Shipyard Full")

    note = fields.Text("note")
    delivery_spot = fields.Many2one("purchase.delivery_spot", string="Delivery Spot")
