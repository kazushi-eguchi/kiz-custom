from odoo import api, fields, models

class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    def reconfigure_product(self):
        """product.configurator.purchaseを上書き"""
        wizard_model = "product.configurator.purchase"
        extra_vals = {
            "order_id": self.order_id.id,
            "order_line_id": self.id,
            "qty": self.product_qty,
            "product_id": self.product_id.id,
        }
        self = self.with_context(
            {
                "default_order_id": self.order_id.id,
                "default_order_line_id": self.id,
            }
        )
        return self.product_id.product_tmpl_id.create_config_wizard(
            model_name=wizard_model, extra_vals=extra_vals
        )