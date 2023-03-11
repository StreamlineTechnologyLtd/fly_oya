from odoo import models, fields, api

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    
    cost_center_id = fields.Many2one(
        comodel_name='cost.center',string='Cost Center', store=True,index=True,auto_join=True,tracking=True, domain = [("children_ids","=",False)], required = True)
    
    department_id = fields.Many2one('hr.department', string = 'Department', store= True, index=True, auto_join=True, tracking=True, domain = [("child_ids","=",False)], required = True)
    
    def _prepare_account_move_line(self, move=False):
        res = super()._prepare_account_move_line(move=False)
        res['cost_center_id'] = self.cost_center_id.id
        res['department_id'] = self.department_id.id
        
        return res

        