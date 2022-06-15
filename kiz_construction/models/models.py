# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kiz_construction(models.Model):
    _name = 'kiz_construction.kiz_construction'
    _description = 'kiz_construction.kiz_construction'
    _rec_name = "no"
    sub_number = fields.Integer("sub number", tracking=True)  # 枝番 OK
    construction_slip_number = fields.Char(string="construction slip number", Transrate=True)  # 制作管理番号 OK
    construction_slip_status = fields.Char(string="construction slip status")  # ステータス OK
    production_management_ticket_period = fields.Date(string="production management ticket period")  # 制作管理票納期 OK
    no = fields.Many2one(
        comodel_name="account.analytic.account", string="production management slip no"
    )  # 制作管理番号 OK
    status = fields.Char(string="status")  # 工事伝票ステータス OK
    deadline = fields.Date(string="deadline")  # 工事伝納期 OK
    account_executive = fields.Char(string="account executive")  # 営業担当者 OK
    trading_company = fields.Many2one(
        comodel_name='res.partner', string='trading_company')  # 商社 OK
    trading_company_short_name = fields.Char(string="trading company short name")  # 商社略称 OK
    branch = fields.Char(string="Branch")  # 支社 OK
    shipyard_full = fields.Char(string="Shipyard Full")  # 造船所 OK
    shipyard_short = fields.Char(string="Shipyard short")  # 造船所略称 OK
    building = fields.Char(string="building")  # 建造所 OK
    s_no = fields.Many2one(
        "ships.ship",
        string="ship"
    )  # S番 OK
    name = fields.Char(string="name")  # 品名 OK
    production_name = fields.Char(string="Production Name")  # 制作名称 OK
    first_category = fields.Char(string="First category")  # 大項目 OK
    second_category = fields.Char(string="Second category")  # 中項目 OK
    ship_class = fields.Char(string="Ship class")  # 船級 OK
    drawing_number = fields.Char(string="drawing number")  # 図面番号 OK
    painting = fields.Char(string="painting")  # 塗装 OK
    product_number = fields.Char(string="product number")  # 品番 OK
    date_of_issue = fields.Datetime(string="date of issue")  # 製作管理票発行日 OK
    finished_making_the_day = fields.Date(string="Finished making the day")  # 製缶完了日 OK
    designer = fields.Char(string="Designer")  # 設計担当者 OK
    machining_drawing = fields.Char(string="Machining drawing")  # 加工図 OK
    in_house_construction_drawing = fields.Char(string="In-house construction drawing")  # 社内工事図 OK
    attachment_id = fields.Many2one('ir.attachment', string="Attachment")  # 添付ファイル OK
    isomorphism = fields.Char(string="Isomorphism")  # 同型 OK
    items = fields.Text(string="items")  # 内訳 OK
    note = fields.Text(string="note")  # 備考 OK
    design_note = fields.Char(string="Design note")  # 設計備考 OK
    nesting_notes = fields.Char(string="Nesting Notes")  # ネスティング備考 OK
    material_input_person = fields.Char(string="Material input person")  # 資材入力者 OK
    production_place = fields.Char(string="Production place")  # 製作場所 OK
    correction_area = fields.Char(string="correction area")  # 手直し場所 OK
    china_arrival_date = fields.Date(string="China arrival date")  # 中国入荷日 OK
    procurement_date = fields.Date(string="Procurement date")  # 調達日 OK
    departure_date = fields.Date(string="Departure date")  # 出港日 OK
    in_days = fields.Integer(string="in days")  # 社内 日間 OK
    in_date = fields.Datetime(string="in date")  # 社内 日付 OK
    china_days = fields.Integer(string="china days")  # 中国 日間 OK
    china_date = fields.Date(string="china date")  # 中国 日付 OK
    consultation_drawing = fields.Binary(string="Consultation drawing")  # 協議図 OK
    approved_drawing = fields.Binary(string="Approved drawing")  # 承認図 OK
    construction_drawing = fields.Binary(string="Construction drawing")  # 工事図 OK
    steel_material_order_date = fields.Date(string="Steel material order date")  # 鋼材注文日 OK
    steel_material_arrangement_date = fields.Date(string="Steel material arrangement date")  # 鋼材手配日 OK
    paint_order_date = fields.Date(string="paint order date")  # 塗装注文日 OK
    paint_arrangement_date = fields.Date(string="paint arrangement date")  # 塗装手配日 OK
    gross_weight = fields.Float(string="Gross weight")  # 予想総重量	OK
    expected_gross_weight = fields.Float(string="Expected gross weight", related='s_no.total_weight')  # 実際重量
    const_files = fields.One2many(
        comodel_name="const.files",
        inverse_name="const_id",
        string="Drawing files", )  # 図面
    purchase_line = fields.One2many(
        comodel_name="purchase.order.line",
        compute='_compute_purchase_line'
    )  # 購買一覧

    # 工数
    installation_f = fields.Float("installation forecast")
    foundation_f = fields.Float("foundation forecast")
    cutting_f = fields.Float("cutting forecast")
    saw_f = fields.Float("saw forecast")
    roll_f = fields.Float("roll forecast")
    press_f = fields.Float("press forecast")
    machining_f = fields.Float("machining forecast")
    robot_f = fields.Float("robot forecast")
    assembly_f = fields.Float("assembly forecast")
    cleaning_f = fields.Float("cleaning forecast")
    weld_f = fields.Float("weld forecast")
    inspection_f = fields.Float("inspection forecast")
    coating_f = fields.Float("coating forecast")
    delivery_f = fields.Float("delivery forecast")
    total_number_of_workers = fields.Float(string="Total number of workers", compute="_calc_total")
    # actual
    installation_a = fields.Float("installation actual")
    foundation_a = fields.Float("foundation actual")
    cutting_a = fields.Float("cutting actual")
    saw_a = fields.Float("saw actual")
    roll_a = fields.Float("roll actual")
    press_a = fields.Float("press actual")
    machining_a = fields.Float("machining actual")
    robot_a = fields.Float("robot actual")
    assembly_a = fields.Float("assembly actual")
    cleaning_a = fields.Float("cleaning actual")
    weld_a = fields.Float("weld actual")
    inspection_a = fields.Float("inspection actual")
    coating_a = fields.Float("coating actual")
    delivery_a = fields.Float("delivery actual")
    total_number_of_workers_2 = fields.Float(string="Total number of workers", compute="_calc_total_2")
    const_process_line_ids = fields.One2many("const.process_line", inverse_name="const_id")

    # 添付ファイル

    # 分析勘定
    # analytic_account_id = fields.Many2one(
    #     comodel_name="account.analytic.account", string="Analytic Account"
    # )

    #     value = fields.Integer()
    #     value2 = fields.Float(compute="_value_pc", store=True)
    #     description = fields.Text()
    #
    #     @api.depends('value')
    #     def _value_pc(self):
    #         for record in self:
    #             record.value2 = float(record.value) / 100

    def create_po(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'purchase.order',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'current',
            'context': {
                'default_name': self.no.name,
                'default_account_id': self.no.id,
                'default_construction_id': self.id,
                'default_s_no': self.s_no.id,
                'default_product_name': self.name,
                'default_trading_company': self.trading_company.id,
                'default_shipyard_full': self.shipyard_full,
            }
        }

    def _compute_purchase_line(self):
        a = self.env["purchase.order.line"].search_read([("account_analytic_id", "=", self.no.name)])
        # b = self.purchase_lines
        print(self.no.name)
        print(a)
        # self.purchase_line = self.env["purchase.order"].search([("account_id", "=", self.no.id)]).id
        self.purchase_line = self.env["purchase.order.line"].search([("account_analytic_id", "=", self.no.name)])
        # print(self.account_id)

    def _calc_total(self):
        for rec in self:
            rec.total_number_of_workers = rec.installation_f + \
                                          rec.foundation_f + \
                                          rec.cutting_f + \
                                          rec.saw_f + \
                                          rec.roll_f + \
                                          rec.press_f + \
                                          rec.machining_f + \
                                          rec.robot_f + \
                                          rec.assembly_f + \
                                          rec.cleaning_f + \
                                          rec.weld_f + \
                                          rec.inspection_f + \
                                          rec.coating_f + \
                                          rec.delivery_f

    def _calc_total_2(self):
        for rec in self:
            rec.total_number_of_workers_2 = rec.installation_a + \
                                            rec.foundation_a + \
                                            rec.cutting_a + \
                                            rec.saw_a + \
                                            rec.roll_a + \
                                            rec.press_a + \
                                            rec.machining_a + \
                                            rec.robot_a + \
                                            rec.assembly_a + \
                                            rec.cleaning_a + \
                                            rec.weld_a + \
                                            rec.inspection_a + \
                                            rec.coating_a + \
                                            rec.delivery_a
