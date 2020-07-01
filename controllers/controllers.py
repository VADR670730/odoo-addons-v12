# -*- coding: utf-8 -*-
from odoo import http

# class Odoo-addons-v12(http.Controller):
#     @http.route('/odoo-addons-v12/odoo-addons-v12/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo-addons-v12/odoo-addons-v12/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo-addons-v12.listing', {
#             'root': '/odoo-addons-v12/odoo-addons-v12',
#             'objects': http.request.env['odoo-addons-v12.odoo-addons-v12'].search([]),
#         })

#     @http.route('/odoo-addons-v12/odoo-addons-v12/objects/<model("odoo-addons-v12.odoo-addons-v12"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo-addons-v12.object', {
#             'object': obj
#         })