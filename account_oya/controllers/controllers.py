# -*- coding: utf-8 -*-
# from odoo import http


# class AccountOya(http.Controller):
#     @http.route('/account_oya/account_oya', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account_oya/account_oya/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('account_oya.listing', {
#             'root': '/account_oya/account_oya',
#             'objects': http.request.env['account_oya.account_oya'].search([]),
#         })

#     @http.route('/account_oya/account_oya/objects/<model("account_oya.account_oya"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account_oya.object', {
#             'object': obj
#         })
