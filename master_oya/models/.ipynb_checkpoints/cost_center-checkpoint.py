# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class master_oya(models.Model):
#     _name = 'master_oya.master_oya'
#     _description = 'master_oya.master_oya'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
