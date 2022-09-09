# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kiz_po_line_check(models.Model):
    _name = 'kiz_po_line_check'
    _description = 'kiz_po_line_check.kiz_po_line_check'



    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
