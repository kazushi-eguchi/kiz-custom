# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kiz_partner(models.Model):
    _inherit = "res.partner"

    code = fields.Char("Code")
    kana = fields.Char("kana")
    alias_name = fields.Char("alias name")
    allocated_code = fields.Char(string="allocated code 1", help="Enter the code assigned by your business partner.")
    allocated_code2 = fields.Char(string="allocated code 2")
    supplier_code = fields.Char(string="supplier code")
    custom_type = fields.Many2many(
        comodel_name="res.partner.custom_type",
    )
    for_purchase = fields.Boolean('')
    for_other_payable = fields.Boolean()
    is_outsourcing_partner = fields.Boolean()
    available = fields.Boolean()
    use_kubun = fields.Boolean()

#    customer
#     partner_code = fields.Many2one("res.partner", string="partner_code")
#     partner_name = fields.Char(related='partner_code.name')
#     name = fields.Char('name')
#     code = fields.Char('code')
#     is_shipyard = fields.Boolean('is_shipyard')
#     is_trading_firm = fields.Boolean('is_trading_firm')
#     fax = fields.Char('fax')
#     cutoff_day = fields.Selection([
#         ('99', '-'),
#         ('10', '10'),
#         ('15', '15'),
#         ('20', '20'),
#         ('25', '25'),
#         ('31', '末'),
#     ], default='',
#         string="cutoff_day")  # カタログ配布 OK Field4__c
#     payment_term = fields.Selection([
#         ('0', '指定なし'),
#         ('1', '当月'),
#         ('2', '翌月'),
#         ('3', '翌々月'),
#         ('4', '翌々月以降'),
#     ], default='',
#         string="payment_term")
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
