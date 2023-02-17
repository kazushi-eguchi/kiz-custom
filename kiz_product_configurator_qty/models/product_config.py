from odoo import _, api, fields, models


class ProductConfigQty(models.TransientModel):
    _inherit = "product.configurator"
    qty = fields.Float('QTY')




