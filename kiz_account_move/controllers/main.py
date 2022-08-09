# -*- coding: utf-8 -*-
# from odoo import http

import json

from odoo.addons.web.controllers.main import CSVExport, ExcelExport
from odoo.http import request

class CSVExportInherit(CSVExport):

    # Override the base() method which is used to gather fields' values in the
    # export CSV.
    def base(self, data, token):
        params = json.loads(data)
        # When the stock.outgoing.shipment.report model is selected, remove
        # the first element in the fields list which is the External ID by
        # default.
        if params["model"] == "account.move.line":
            data = json.dumps(params)
            for line in params["ids"]:
                rec = request.env["account.move.line"].browse(line)
                rec.write({"exported": True})
        return super(CSVExportInherit, self).base(data, token)


class ExcelExportInherit(ExcelExport):

    # Override the base() method which is used to gather fields' values in the
    # export Excel.
    def base(self, data, token):
        params = json.loads(data)
        # When the stock.outgoing.shipment.report model is selected, remove
        # the first element in the fields list which is the External ID by
        # default.
        if params["model"] == "account.move.line" and params["ids"]:
            data = json.dumps(params)
            for line in params["ids"]:
                rec = request.env["account.move.line"].browse(line)
                rec.write({"exported": True})
        return super(ExcelExportInherit, self).base(data, token)
# class KizAccountMove(http.Controller):
#     @http.route('/kiz_account_move/kiz_account_move/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kiz_account_move/kiz_account_move/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kiz_account_move.listing', {
#             'root': '/kiz_account_move/kiz_account_move',
#             'objects': http.request.env['kiz_account_move.kiz_account_move'].search([]),
#         })

#     @http.route('/kiz_account_move/kiz_account_move/objects/<model("kiz_account_move.kiz_account_move"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kiz_account_move.object', {
#             'object': obj
#         })
