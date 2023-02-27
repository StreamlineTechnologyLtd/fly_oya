# -*- coding: utf-8 -*-
# from odoo import http


# class MasterOya(http.Controller):
#     @http.route('/master_oya/master_oya', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/master_oya/master_oya/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('master_oya.listing', {
#             'root': '/master_oya/master_oya',
#             'objects': http.request.env['master_oya.master_oya'].search([]),
#         })

#     @http.route('/master_oya/master_oya/objects/<model("master_oya.master_oya"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('master_oya.object', {
#             'object': obj
#         })
