# -*- coding: utf-8 -*-
# from odoo import http


# class Staging1Module(http.Controller):
#     @http.route('/staging1_module/staging1_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/staging1_module/staging1_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('staging1_module.listing', {
#             'root': '/staging1_module/staging1_module',
#             'objects': http.request.env['staging1_module.staging1_module'].search([]),
#         })

#     @http.route('/staging1_module/staging1_module/objects/<model("staging1_module.staging1_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('staging1_module.object', {
#             'object': obj
#         })
