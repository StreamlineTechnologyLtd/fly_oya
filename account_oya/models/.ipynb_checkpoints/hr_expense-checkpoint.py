import re
from markupsafe import Markup
from odoo import api, fields, Command, models, _
from odoo.tools import float_round
from odoo.exceptions import UserError, ValidationError
from odoo.tools import email_split, float_is_zero, float_repr, float_compare, is_html_empty
from odoo.tools.misc import clean_context, format_date

class HrExpense(models.Model):
    _inherit = 'hr.expense'
    cost_center_id = fields.Many2one(
        comodel_name='cost.center',string='Cost Center', store=True,index=True,auto_join=True,tracking=True, domain = [("children_ids","=",False)])
    department_id = fields.Many2one('hr.department', string = 'Department', store= True, index=True,auto_join=True,tracking=True,
                                    domain = [("child_ids","=",False)])

    
    def _get_split_values(self):
        self.ensure_one()
        half_price = self.total_amount / 2
        price_round_up = float_round(half_price, precision_digits=2, rounding_method='UP')
        price_round_down = float_round(half_price, precision_digits=2, rounding_method='DOWN')

        return [{
            'name': self.name,
            'product_id': self.product_id.id,
            'total_amount': price,
            'tax_ids': self.tax_ids.ids,
            'currency_id': self.currency_id.id,
            'company_id': self.company_id.id,
            'analytic_distribution': self.analytic_distribution,
            'cost_center_id': self.cost_center_id.id,
            'department_id': self.department_id.id,
            'employee_id': self.employee_id.id,
            'expense_id': self.id,
        } for price in [price_round_up, price_round_down]]
    
    
    
    def action_move_create(self):
        '''
        main function that is called when trying to create the accounting entries related to an expense
        '''
        moves = self.env['account.move'].create([
            {
                'journal_id': (
                    sheet.bank_journal_id
                    if sheet.payment_mode == 'company_account' else
                    sheet.journal_id
                ).id,
                'move_type': 'in_receipt',
                'company_id': sheet.company_id.id,
                'partner_id': sheet.employee_id.sudo().address_home_id.commercial_partner_id.id,
                'date': sheet.accounting_date or fields.Date.context_today(sheet),
                'invoice_date': sheet.accounting_date or fields.Date.context_today(sheet),
                'ref': sheet.name,
                # force the name to the default value, to avoid an eventual 'default_name' in the context
                # to set it to '' which cause no number to be given to the account.move when posted.
                'name': '/',
                'expense_sheet_id': [Command.set(sheet.ids)],
                'line_ids':[
                    Command.create({
                        'name': expense.employee_id.name + ': ' + expense.name.split('\n')[0][:64],
                        'account_id': expense.account_id.id,
                        'quantity': expense.quantity or 1,
                        'price_unit': expense.unit_amount if expense.unit_amount != 0 else expense.total_amount,
                        'product_id': expense.product_id.id,
                        'product_uom_id': expense.product_uom_id.id,
                        'analytic_distribution': expense.analytic_distribution,
                        'expense_id': expense.id,
                        'partner_id': expense.employee_id.sudo().address_home_id.commercial_partner_id.id,
                        'tax_ids': [(6, 0, expense.tax_ids.ids)],
                        'currency_id': expense.currency_id.id,
                        'cost_center_id': expense.cost_center_id.id,
                        'department_id': expense.department_id.id
                    })
                    for expense in sheet.expense_line_ids
                ]
            }
            for sheet in self.sheet_id
        ])
        moves._post()

        for expense in self:
            if expense.payment_mode == 'company_account':
                expense.sheet_id.paid_expense_sheets()

        return {move.expense_sheet_id.id: move for move in moves}
    
    
    

class HrExpenseSplit(models.TransientModel):
    _inherit = 'hr.expense.split'
    
    cost_center_id = fields.Many2one(
        comodel_name='cost.center',string='Cost Center', store=True,index=True,auto_join=True,tracking=True, domain = [("children_ids","=",False)])
    department_id = fields.Many2one('hr.department', string = 'Department', store= True, index=True,auto_join=True,tracking=True, domain = [("child_ids","=",False)])
    
    
    def default_get(self, fields):
        result = super().default_get(fields)
        if 'expense_id' in result:
            result['cost_center_id'] = expense.cost_center_id
            result['department_id'] = expense.department_id
        return result
    
    
    
    def _get_values(self):
        result = super()._get_values()
        result['cost_center_id'] = self.cost_center_id.id
        result['department_id'] = self.department_id.id

        return result
       