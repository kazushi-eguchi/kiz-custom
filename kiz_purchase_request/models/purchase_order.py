# # -*- coding: utf-8 -*-
#
from odoo import models, fields, api


#
#


class KizPurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    #
    account_id = fields.One2many(
        comodel_name="account.analytic.account", compute='_compute_account_id'
    )

    def _compute_account_id(self):

        a = self.env["purchase.order.line"].search_read([], [])
        #b = self.purchase_lines
        print(self.id)
        print(a)
        self.account_id = self.env["purchase.order.line"].search([("order_id", "=", self.id)]).account_analytic_id
        print(self.account_id)

