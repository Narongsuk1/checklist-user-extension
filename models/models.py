# -*- coding: utf-8 -*-

from odoo import models, fields, api

class checklist_user(models.Model):
    _name = 'checklist.checklist'
    _inherit = 'checklist.checklist'
    showall = fields.Boolean(string="Show All User",help="Do you want to show this task to all user?")
    # domain=['|',('create_uid','=',False),('create_uid','=',user.id)]
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100