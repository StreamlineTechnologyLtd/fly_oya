# -*- coding: utf-8 -*-
# from odoo import http


# class HrPortal(http.Controller):
#     @http.route('/hr_portal/hr_portal', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_portal/hr_portal/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_portal.listing', {
#             'root': '/hr_portal/hr_portal',
#             'objects': http.request.env['hr_portal.hr_portal'].search([]),
#         })

#     @http.route('/hr_portal/hr_portal/objects/<model("hr_portal.hr_portal"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_portal.object', {
#             'object': obj
#         })
