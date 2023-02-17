from odoo import _, api, fields, models


class ProductConfiguratorPurchaseQty(models.TransientModel):
    _name = "product.configurator.purchase.qty"
    _inherit = "product.configurator.purchase"
    _description = "Product Configurator Purchase Qty"

    qty = fields.Float()

    def _get_order_line_vals(self, product_id):
        print("test")
        return super(ProductConfiguratorPurchaseQty, self)._get_order_line_vals(product_id)

    # """Hook to allow custom line values to be put on the newly
    #         created or edited lines."""
    # product = self.env["product.product"].browse(product_id)
    # return {
    #     "product_id": product_id,
    #     "product_qty": self.qty,
    #     "name": product._get_mako_tmpl_name(),
    #     "product_uom": product.uom_id.id,
    #     "date_planned": fields.Datetime.now(),
    #     "config_session_id": self.config_session_id.id,
    #     "price_unit": self.config_session_id.price,
    # }
