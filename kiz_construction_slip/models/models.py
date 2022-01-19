# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kiz_construction_slip(models.Model):
    _name = 'kiz_construction_slip.kiz_construction_slip'
    _description = 'kiz_construction_slip.kiz_construction_slip'

    # name = fields.Char(sting="construction slip no")
    analytic_account_id = fields.Many2one(
        comodel_name="account.analytic.account", string="production management slip no",
        require="true",
    )
    status = fields.Char(string="status")  # 工事伝票ステータス
    deadline = fields.Date(string="deadline")  # 工事伝納期
    account_executive = fields.Char(string="account executive")  # 営業担当者
    trading_company = fields.Many2one('res.company', string='Company')  # 商社
    trading_company_short_name = fields.Char(string="trading company short name")  # 商社略称
    branch = fields.Char(string="Branch")  # 支社
    shipyard_full = fields.Char(string="Shipyard Full")
    shipyard_short = fields.Char(string="Shipyard short")
    building = fields.Char(string="building")
    s_no = fields.Many2one(
        "ships.ship",
        string="ship"
    )  # S番
    production_name = fields.Char(string="Production Name")
    first_category = fields.Char(string="First category")
    second_category = fields.Char(string="Second category")
    ship_class = fields.Char(string="Ship class")
    drawing_number = fields.Char(string="drawing number")
    painting = fields.Char(string="painting")
    product_number = fields.Char(string="product number")
    date_of_issue = fields.Date(string="date of issue")
    attachment_id = fields.Many2one('ir.attachment', string="Attachment")
    gross_weight = fields.Integer(string="Gross weight")
    expected_gross_weight = fields.Integer(string="Expected gross weight")
    breakdown = fields.Text(string="breakdown")
    remarks = fields.Text(string="remarks")
    note = fields.Text(string="note")

    #     value = fields.Integer()
    #     value2 = fields.Float(compute="_value_pc", store=True)
    #     description = fields.Text()
    #
    #     @api.depends('value')
    #     def _value_pc(self):
    #         for record in self:
    #             record.value2 = float(record.value) / 100
    @api.model
    def create(self, vals):
        print("val", vals)
        print(vals["analytic_account_id"])
        if vals["analytic_account_id"] == False:
            account = self.env['account.analytic.account'].create({'name': "247",
                                                               'company_id': vals.get(
                                                                   'company_id') or self.env.company.id,
                                                               'partner_id': vals.get('partner_id'),
                                                               'active': True,
                                                               })

            self.env['kiz_construction.kiz_construction'].create({'no': account.id,
                                                                  })
            vals["analytic_account_id"] = account.id
        else:
            self.env['kiz_construction.kiz_construction'].create({'no': vals["analytic_account_id"],
                                                                  })

        #print(account.id)
        res = super(kiz_construction_slip, self).create(vals)
        return res
