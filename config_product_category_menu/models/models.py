# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class config_product_category_menu(models.Model):
#     _name = 'config_product_category_menu.config_product_category_menu'
#     _description = 'config_product_category_menu.config_product_category_menu'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
