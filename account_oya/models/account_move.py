
from odoo import models, fields, api
from odoo.osv import expression

class AccountMoveLine(models.Model):
    
    _inherit = ["account.move.line"]
    
    cost_center_id = fields.Many2one(
        comodel_name='cost.center',string='Cost Center', store=True,index=True,auto_join=True,tracking=True, domain = [("children_ids","=",False)])
    department_id = fields.Many2one('hr.department', string = 'Department', store= True, index=True,auto_join=True,tracking=True, domain = [("child_ids","=",False)])
    


class AccountMove(models.Model):
    _inherit = ["account.move"]
    
    @api.model
    def _prepare_move_for_asset_depreciation(self, vals):
        missing_fields = set(['asset_id', 'amount', 'depreciation_beginning_date', 'date', 'asset_number_days']) - set(vals)
        if missing_fields:
            raise UserError(_('Some fields are missing {}').format(', '.join(missing_fields)))
        asset = vals['asset_id']
        analytic_distribution = asset.analytic_distribution
        depreciation_date = vals.get('date', fields.Date.context_today(self))
        company_currency = asset.company_id.currency_id
        current_currency = asset.currency_id
        prec = company_currency.decimal_places
        amount_currency = vals['amount']
        amount = current_currency._convert(amount_currency, company_currency, asset.company_id, depreciation_date)
        # Keep the partner on the original invoice if there is only one
        partner = asset.original_move_line_ids.mapped('partner_id')
        partner = partner[:1] if len(partner) <= 1 else self.env['res.partner']
        move_line_1 = {
            'name': asset.name,
            'partner_id': partner.id,
            'account_id': asset.account_depreciation_id.id,
            'debit': 0.0 if float_compare(amount, 0.0, precision_digits=prec) > 0 else -amount,
            'credit': amount if float_compare(amount, 0.0, precision_digits=prec) > 0 else 0.0,
            'analytic_distribution': analytic_distribution,
            'currency_id': current_currency.id,
            'amount_currency': -amount_currency,
            'cost_center_id': asset.cost_center_id.id,
            'department_id': asset.department_id.id
        }
        move_line_2 = {
            'name': asset.name,
            'partner_id': partner.id,
            'account_id': asset.account_depreciation_expense_id.id,
            'credit': 0.0 if float_compare(amount, 0.0, precision_digits=prec) > 0 else -amount,
            'debit': amount if float_compare(amount, 0.0, precision_digits=prec) > 0 else 0.0,
            'analytic_distribution': analytic_distribution,
            'currency_id': current_currency.id,
            'amount_currency': amount_currency,
            'cost_center_id': asset.cost_center_id.id,
            'department_id': asset.department_id.id
        }
        move_vals = {
            'partner_id': partner.id,
            'date': depreciation_date,
            'journal_id': asset.journal_id.id,
            'line_ids': [(0, 0, move_line_1), (0, 0, move_line_2)],
            'asset_id': asset.id,
            'ref': _("%s: Depreciation", asset.name),
            'asset_depreciation_beginning_date': vals['depreciation_beginning_date'],
            'asset_number_days': vals['asset_number_days'],
            'name': '/',
            'asset_value_change': vals.get('asset_value_change', False),
            'move_type': 'entry',
            'currency_id': current_currency.id,
        }
        
        return move_vals
    
    
