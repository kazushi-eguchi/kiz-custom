# -*- coding: utf-8 -*-

from odoo import models, fields, api


class KizPurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    #

    def print_quotation(self):
        # self.write({'state': "sent"})
        return self.env.ref('purchase.report_purchase_quotation').report_action(self)
