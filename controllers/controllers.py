# -*- coding: utf-8 -*-
from odoo import http

# class ChecklistUser(http.Controller):
#     @http.route('/checklist_user/checklist_user/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/checklist_user/checklist_user/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('checklist_user.listing', {
#             'root': '/checklist_user/checklist_user',
#             'objects': http.request.env['checklist_user.checklist_user'].search([]),
#         })

#     @http.route('/checklist_user/checklist_user/objects/<model("checklist_user.checklist_user"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('checklist_user.object', {
#             'object': obj
#         })