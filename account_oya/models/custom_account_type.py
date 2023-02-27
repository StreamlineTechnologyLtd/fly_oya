from odoo import models, fields, api
from odoo.osv import expression

class CustomAccountType(models.Model):
    
    _name = "custom.account.type"