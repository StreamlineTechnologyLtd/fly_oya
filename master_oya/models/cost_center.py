# -*- coding: utf-8 -*-
from collections import defaultdict
from odoo import api, fields, models, _
from odoo.osv import expression
from random import randint



class master_oya(models.Model):
    _name = 'cost.center'
    _inherit = ['mail.thread']
    _description = 'Cost Center'
    _rec_name = 'complete_name'
    _order = 'complete_name asc'
    
    def _default_color(self):
        return randint(1, 11)
    
    name = fields.Char(string = "Name", index='trigram', required = True)
    code = fields.Char(string = "Code", required=True, tracking=True)
    description = fields.Text(string='Description')
    company_id = fields.Many2one('res.company', string = "Company")
    parent_id = fields.Many2one('cost.center', string = "Parent Cost Center",  ondelete='cascade')
    children_ids = fields.One2many('cost.center', 'parent_id', string = "Parent Cost Center")
    children_count = fields.Integer(
        'Children Plans Count',
        compute='_compute_children_count',
    )
    complete_name = fields.Char(
        'Complete Name',
        compute='_compute_complete_name',
        recursive=True,
        store=True,
    )
    color = fields.Integer('Color',
        default=_default_color)
    
    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = ['|', ('code', '=ilike', name.split(' ')[0] + '%'), ('name', operator, name)]
            if operator in expression.NEGATIVE_TERM_OPERATORS:
                domain = ['&', '!'] + domain[1:]
        return self._search(expression.AND([domain, args]), limit=limit, access_rights_uid=name_get_uid)

    
    def name_get(self):
        result = []
        for account in self:
            name = account.code + ' ' + account.complete_name
            result.append((account.id, name))
        return result
    
    
    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for cost in self:
            if cost.parent_id:
                cost.complete_name = '%s / %s' % (cost.parent_id.complete_name, cost.name)
            else:
                cost.complete_name = cost.name
                
    
    @api.depends('children_ids')
    def _compute_children_count(self):
        for cost in self:
            cost.children_count = len(cost.children_ids)
    
    
    def action_view_children_cost_centers(self):
        result = {
            "type": "ir.actions.act_window",
            "res_model": "cost.center",
            "domain": [('id', 'in', self.children_ids.ids)],
            "context": {'default_parent_id': self.id,
                        'default_color': self.color},
            "name": _("Cost Center"),
            'view_mode': 'list,form',
        }
        return result
    
    
