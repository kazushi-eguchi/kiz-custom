from odoo import fields, models


class ProductTemplateAccountFields(models.Model):
    _inherit = "product.template"

    kubun = fields.Char("区分")
