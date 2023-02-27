# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountAccount(models.Model):
    _inherit = ["account.account"]


    account_type = fields.Selection(
        selection=[
            ("asset_receivable", "Receivable"),
            ("asset_cash", "Bank and Cash"),
            ("asset_current", "Inventory"),
            ("asset_non_current", "Non-current Assets"),
            ("asset_prepayments", "Prepayments"),
            ("asset_fixed", "Fixed Assets"),
            ("liability_payable", "Payable"),
            ("liability_credit_card", "Credit Card"),
            ("liability_current", "Current Liabilities"),
            ("liability_non_current", "Non-current Liabilities"),
            ("equity", "Equity"),
            ("equity_unaffected", "Current Year Earnings"),
            ("income", "Revenue"),
            ("income_other", "Other Revenue"),
            ("income_cr", "Cargo Revenue"),
            ("income_otr", "Other Transport Revenues"),
            ("income_ntr", "Non-Transport Revenue"),
            ("cor_ac", "Aircraft Cost"),
            ("cor_foc", "Flight Operations Cost"),
            ("cor_prc", "Passenger Related Cost"),
            ("cor_cc", "Crew Cost"),
            ("cor_cgc", "Cargo Cost"),
            ("cor_se", "Sales Expenses"),
            ("expense", "Expenses"),
            ("expense_depreciation", "Depreciation"),
            ('expense_tc','Transport Cost'),
('expense_lr','Lease and Rent'),
('expense_oe','Office Expenses'),
('expense_hse','Health Safety & Environment'),
('expense_ite','IT Expenses'),
('expense_depreciation','Depreciation'),
('expense_plf','Professional and Legal Fees'),
('expense_fe','Financial Expenses'),
('expense_tax','Tax'),
            ("expense_direct_cost", "Cost of Revenue"),
            ("off_balance", "Off-Balance Sheet"),
        ],
        string="Type",
        help="These types are defined according to your country. The type contains more information "\
        "about the account and its specificities."
    )
    internal_group = fields.Selection(selection_add=[('cor', 'Cost Of Revenue')])

# class account_oya(models.Model):
#     _name = 'account_oya.account_oya'
#     _description = 'account_oya.account_oya'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
