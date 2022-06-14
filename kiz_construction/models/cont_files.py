# -*- coding: utf-8 -*-

from odoo import models, fields, api
from wand.image import Image
from wand.color import Color
import base64

class ConstFiles(models.Model):
    _name = "const.files"
    _description = "Const Files"
    _order = "id"

    const_id = fields.Many2one('kiz_construction.kiz_construction', 'Construction')
    name = fields.Char("File Name")
    file = fields.Binary(string="file")
    image = fields.Binary()
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

    @api.model
    def create(self, values):
        att = super(ConstFiles, self).create(values)
        # ~ if self._context.get('convert') == 'pdf2image' and att.mimetype == 'application/pdf':
        # if att.file_type == 'application/pdf':
        att.pdf2image(800, 1200)
        return att

    # @api.depends('name', 'file')
    def pdf2image(self, dest_width, dest_height):
        RESOLUTION = 300
        if self.file:
            print(self.file)
            # image = Image(blob=self.file.decode(), resolution=(RESOLUTION, RESOLUTION))
            image = Image(blob=base64.b64decode(self.file), resolution=(RESOLUTION, RESOLUTION))
            # image.background_color = Color('white')
            # image.resize(dest_width, dest_height)
            print(image)
            self.image = base64.b64encode(image.make_blob(format='jpg'))
            # self.image = image.make_blob(format='jpg').encode('base64')