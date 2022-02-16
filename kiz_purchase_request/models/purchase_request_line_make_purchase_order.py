# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseRequestLineMakePurchaseOrder(models.TransientModel):
    _inherit = "purchase.request.line.make.purchase.order"

    @api.model
    def _prepare_purchase_order(self, picking_type, group_id, company, origin):
        active_model = self.env.context.get("active_model")
        print("test")
        data = super()._prepare_purchase_order(picking_type, group_id, company, origin)
        request_ids = []
        if active_model == "purchase.request.line":
            request_line_ids = self.env.context.get("active_ids", [])
            request_ids += (
                self.env[active_model].browse(request_line_ids).mapped("request_id.id")
            )
        elif active_model == "purchase.request":
            request_ids += self.env.context.get("active_ids", [])
        if not request_ids:
            return data
        request = self.env["purchase.request"].browse(request_ids)[:1]
        data["account_id"] = request.account_id.id
        return data