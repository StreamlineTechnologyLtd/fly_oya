from odoo import models, fields, api

class AccountAsset(models.Model):
    _inherit = 'account.asset'
    
    cost_center_id = fields.Many2one(
        comodel_name='cost.center',string='Cost Center', store=True,index=True,auto_join=True,tracking=True, domain = [("children_ids","=",False)], required = True)
    department_id = fields.Many2one('hr.department', string = 'Department', store= True, index=True,auto_join=True,tracking=True, domain = [("child_ids","=",False)], required = True)
    
    asset_type = fields.Selection([('sale', 'Sale: Revenue Recognition'), ('purchase', 'Purchase: Asset'), ('expense', 'Deferred Expense')], compute='_compute_asset_type', store=True, index=True, copy=True, change_default=True)

        