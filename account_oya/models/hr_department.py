from odoo import api, fields, Command, models, _
from collections import defaultdict
from odoo.osv import expression
from random import randint

class Department(models.Model):
    _inherit = ["hr.department"]
    _rec_name = 'name'
    
    code = fields.Char(string = "Code", required=True, tracking=True, default = " ")
    
    
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
        return [(record.id, record.code + " " + record.complete_name ) for record in self]
