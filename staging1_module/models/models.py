# -*- coding: utf-8 -*-

from odoo import models, fields, api


class staging1_module(models.Model):
    _name = 'staging1.module'
    _description = 'staging1_module.staging1_module'

    name = fields.Char()
    value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
