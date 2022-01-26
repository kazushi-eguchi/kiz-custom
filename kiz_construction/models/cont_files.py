# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ConstFiles(models.Model):
    _name = "const.files"
    _description = "Const Files"
    _order = "id"

    const_id = fields.Many2one('kiz_construction.kiz_construction', 'Construction')
    name = fields.Char("File Name")
    file = fields.Binary(string="file")
    image = fields.Binary(compute='_compute_file_image')
    type = fields.Selection(
        [('field', 'Drawings for the field'),
         ('delivery', 'Drawings for delivery'),
         ('painting', 'Drawings for painting'),
         ('qc', 'Drawings for quality control'),
         ('inspection', 'Drawing for inspection'),
         ('Bead', 'Bead Character Drawing'),
         ('hirokei', 'Drawings for hirokei'),
         ],
    )

    # @api.depends('name', 'file')
    # def _compute_file_image(self):
    #     RESOLUTION = 300
    #     self.image = Image(blob=self.datas.decode('base64'),resolution=(RESOLUTION,RESOLUTION))
