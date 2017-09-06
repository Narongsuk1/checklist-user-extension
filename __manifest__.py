# -*- coding: utf-8 -*-
{
    'name': "checklist_user",

    'summary': """
        checklist for grant permission to user""",

    'description': """
        checklist for grant permission to user. required checklist module.
    """,

    'author': "O",
    'website': "http://www.medvine.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
            'base',
            'checklist',
            'report'
    ],

    # always loaded
    'data': [
        'views/views.xml',
        'report/checklist_user_report.xml'
    ],
}