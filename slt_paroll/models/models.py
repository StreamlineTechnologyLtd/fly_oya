# -*- coding: utf-8 -*-

from odoo import models, fields, api




class HrPayslip(models.Model):
    _inherit = 'hr.payslip'
    
    def _get_default_currency_id(self):
        return self.env.company.currency_id.id
    
    
    sto = fields.Float(string='STO days') 
    uto = fields.Float(string='UTO days') 
    bouns_over_time = fields.Float(string='Overtime hours') 
    
            
            
            
            
class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    guarantee = fields.Float(string='Guarantee', config_parameter = 'payroll.guarantee') #ضمان
    solidarity = fields.Float(string='Solidarity', config_parameter = 'payroll.solidarity') #تضامن
    symbiosis = fields.Float(string='Symbiosis', config_parameter = 'payroll.symbiosis')#تكافل
    employer = fields.Float(string='Employer', config_parameter = 'payroll.employer') # حصة جهة العمل
    jihad = fields.Float(string='Jihad', config_parameter = 'payroll.jihad') #جهاد
    dinar = fields.Float(string='dinar', config_parameter = 'payroll.dinar') #دينار
    subsidies = fields.Float(string='Subsidies', config_parameter = 'payroll.subsidies') #اعانات
    damgha = fields.Float(string='damgha', config_parameter = 'payroll.damgha') #
    syndicate = fields.Float(string='syndicate', config_parameter = 'payroll.syndicate') #
    

class HrEmployeeInhert(models.Model):
    _inherit = 'hr.employee'
    
    def _get_default_currency_id(self):
        return self.env.company.currency_id.id
    
    housing_allowance = fields.Integer(string='Housing allowance') #اعانات
    job_bonus = fields.Integer(string='Job bonus') 
    # treasury_bonus = fields.Monetary(string='Treasury bonus',currency_field="currency_id") 
    # family_allowance = fields.Monetary(string='Family Allowance',currency_field="currency_id") 
    # continuous_additional = fields.Monetary(string='Continuous Additional',currency_field="currency_id") 
    # non_continuous_additional = fields.Monetary(string='Non continuous additional',currency_field="currency_id")
    # continuous_deductions = fields.Monetary(string='continuous deduction',currency_field="currency_id")
    # liability_premium = fields.Monetary(string='Liability premium',currency_field="currency_id") 
    # monthly_difference = fields.Monetary(string='Monthly difference',currency_field="currency_id") 
    # commission_bonus = fields.Monetary(string='Commission bonus',currency_field="currency_id") 
    # other_allowances = fields.Monetary(string='Ather Allowances',currency_field="currency_id") 
        
class HrPayslip(models.Model):
    _inherit = 'hr.contract'
    
    
    @api.depends('exemption','employee_id.children','employee_id.marital')
    def _exemption(self):
        for record in self:
            if self.employee_id.marital ==  'married':
                record['exemption'] = 200+(self.employee_id.children*25)  
            else :
                record['exemption'] = 150
    
    
    exemption = fields.Float(string='Exemption',currency_field="currency_id" ,compute = '_exemption') #
    
    @api.depends()
    def _compute_value(self):
        for record in self:
              
            record['guarantee'] =  self.env['ir.config_parameter'].sudo().get_param('payroll.guarantee')
            record['solidarity'] =  self.env['ir.config_parameter'].sudo().get_param('payroll.solidarity')
            record['symbiosis'] =  self.env['ir.config_parameter'].sudo().get_param('payroll.symbiosis') #تكافل
            record['employer'] =  self.env['ir.config_parameter'].sudo().get_param('payroll.employer') #حصة جهة العمل
            record['jihad'] =  self.env['ir.config_parameter'].sudo().get_param('payroll.jihad')
            record['damgha'] = self.env['ir.config_parameter'].sudo().get_param('payroll.damgha')
            record['subsidies'] = self.env['ir.config_parameter'].sudo().get_param('payroll.subsidies') #اعانات 
            record['dinar'] = self.env['ir.config_parameter'].sudo().get_param('payroll.dinar')
            
            
    @api.depends('new_wage','wage','exemption','guarantee','solidarity')
    def _compute_value2(self):
        for record in self:
            if self.wage > 1000:
                record['new_wage'] = ((self.wage -(0.1*self.exemption)-50))/(0.87*(1-((self.guarantee+self.solidarity)/100)))
            else :
                record['new_wage'] = (self.wage -(0.05*self.exemption))/(0.92*(1-((self.guarantee+self.solidarity)/100)))
                 
    # net_sulary = fields.Integer(string='Net Sulary')
    un_taxble_wage = fields.Monetary(string='Untaxble Wage',currency_field="currency_id")
    new_wage = fields.Monetary('Wage', required=True, tracking=True, help="Employee's monthly gross wage.",compute = '_compute_value2')

    dinar = fields.Float(string='Dinar',currency_field="currency_id",compute = '_compute_value') #دينار
    guarantee =fields.Float(string='Guarantee',currency_field="currency_id",compute = '_compute_value') #ضمان
    solidarity = fields.Float(string='Solidarity',currency_field="currency_id",compute = '_compute_value') #تضامن
    symbiosis = fields.Float(string='Symbiosis',currency_field="currency_id",compute = '_compute_value') #تكافل
    employer = fields.Float(string='Employer',currency_field="currency_id",compute = '_compute_value') #حصة
    jihad = fields.Float(string='Jihad',currency_field="currency_id",compute = '_compute_value') #جهاد
    subsidies = fields.Float(string='Subsidies',currency_field="currency_id",compute = '_compute_value')#الاعانات
    damgha = fields.Float(string='damgha',currency_field="currency_id",compute = '_compute_value') #
            