# -*- coding: utf-8 -*-

from odoo import models, fields, api

class checklist_user(models.Model):
    _name = 'checklist.checklist'
    _inherit = 'checklist.checklist'
    showall = fields.Boolean(string="Show All User",help="Do you want to show this task to all user?")
   