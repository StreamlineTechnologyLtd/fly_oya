# -*- coding: utf-8 -*-
# from odoo import http


# class SltParoll(http.Controller):
#     @http.route('/slt_paroll/slt_paroll', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/slt_paroll/slt_paroll/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('slt_paroll.listing', {
#             'root': '/slt_paroll/slt_paroll',
#             'objects': http.request.env['slt_paroll.slt_paroll'].search([]),
#         })

#     @http.route('/slt_paroll/slt_paroll/objects/<model("slt_paroll.slt_paroll"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('slt_paroll.object', {
#             'object': obj
#         })
