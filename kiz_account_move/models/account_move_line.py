# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kiz_account_move(models.Model):
    _inherit = 'account.move.line'

    today_id = fields.Char("ID(編集不可)")
    invoice_deliver_date = fields.Date(string="請求書納品日", store=True)
    # rate = fields.Float("レート", default=1)
    rate = fields.Float("為替レート", compute="_get_rate")
    jma_order_no_ref = fields.Char("JMU注番", compute="_get_jma_order_no")
    supplier_line = fields.Char("仕入先", compute="_get_supplier_line")
    display_id = fields.Integer("件名", related="id")
    po_no = fields.Char("仕入れコード", compute="_get_po_no")
    # po_no = fields.Char("仕入れコード")
    size = fields.Text("サイズ", compute="_get_size")
    kubun = fields.Text("区分", compute="_get_kubun")
    display_move_id = fields.Char("仕入コード")
    # display_move_id = fields.Integer("仕入コード", compute="_get_move_id")
    tax = fields.Char("消費税", compute="_get_tax")
    price = fields.Char("単価")
    price_total_cp = fields.Char("金額")
    summary = fields.Text("摘要")
    hinmei = fields.Char("品名", related="product_id.name")
    # kouji_id = fields.Char("工事伝票番号", related="analytic_account_id.name")
    kouji_id = fields.Char("工事伝票番号", compute="_get_kouji_id")
    yotei_date = fields.Date("支払予定日", related="date")
    qty = fields.Char("数量")
    uom = fields.Char("単位")

    def _get_kouji_id(self):
        for rec in self:
            no = str(self.env['purchase.order'].search([('name', '=', rec.move_id.invoice_origin)]).construction_id.no.name)
            sub_no = str(self.env['purchase.order'].search([('name', '=', rec.move_id.invoice_origin)]).construction_id.sub_number).zfill(2)
            rec.kouji_id = no + "-" + sub_no
            # if rec.product_id.kubun:
            #     print("id", rec.move_id.purchase_id)
            #     rec.kouji_id = rec.move_id.purchase_id.account_id.name
            # else:
            #     rec.kouji_id = rec.analytic_account_id.name

    def _get_rate(self):
        for rec in self:
            if rec.move_id.default_rate:
                rec.rate = rec.move_id.default_rate
            else:
                rec.jma_order_no_ref = "1"

    def _get_tax(self):
        for rec in self:
            if rec.product_id.kubun:
                if "消費税" in rec.product_id.kubun:
                    rec.tax = str(rec.price_subtotal)
                    rec.price = ""
                    rec.price_total_cp = ""
                    rec.kouji_id = rec.analytic_account_id.name
            else:
                rec.tax = ""
                rec.price = str(rec.price_subtotal)
                rec.price_total_cp = str(rec.price_unit * rec.quantity)
                rec.qty = str(rec.quantity)
                rec.uom = str(rec.product_uom_id.name)

    def _get_rate(self):
        for rec in self:
            if rec.move_id.default_rate:
                rec.rate = rec.move_id.default_rate
            else:
                rec.jma_order_no_ref = "1"

    def _get_move_id(self):
        for rec in self:
            if rec.move_id.id:
                rec.display_move_id = rec.move_id.id
            else:
                rec.display_move_id = False

    def _get_jma_order_no(self):
        for rec in self:
            if rec.move_id.jma_order_no:
                rec.jma_order_no_ref = rec.move_id.jma_order_no
            else:
                rec.jma_order_no_ref = ""

    def _get_supplier_line(self):
        for rec in self:
            if rec.move_id.partner_id:
                if rec.move_id.partner_id.code and rec.move_id.partner_id.name:
                    rec.supplier_line = rec.move_id.partner_id.code + " : " + rec.move_id.partner_id.name
                else:
                    rec.supplier_line = ""
            else:
                rec.supplier_line = ""

    def _get_po_no(self):
        for rec in self:
            if rec.purchase_order_id.name:
                rec.po_no = rec.purchase_order_id.name
            #     rec.po_no = False
            else:
                rec.po_no = ""

    def _get_size(self):
        for rec in self:
            item = []
            if rec.name:
                for l in rec.product_id.product_template_attribute_value_ids:
                    if l.attribute_id.product_name and l.name:
                        # item = item + " " + l.attribute_id.product_name + ":" + l.name
                        item.append(l.attribute_id.product_name + ":" + l.name)
                    elif l.attribute_id.name and l.name:
                        # item = item + " " + l.attribute_id.name + ":" + l.name
                        item.append(l.attribute_id.name + ":" + l.name)
                for l in rec.purchase_line_id.config_session_id.custom_value_ids:
                    if l.attribute_id.product_name and l.value:
                        # item = item + " " + l.attribute_id.product_name + ":" + l.value
                        item.append(l.attribute_id.product_name + ":" + l.value)
                rec.size = "／".join(item)
            else:
                rec.size = "／".join(item)

    def _get_kubun(self):
        for rec in self:
            if rec.product_id.kubun:
                rec.kubun = rec.product_id.kubun
            else:
                rec.kubun = ""
