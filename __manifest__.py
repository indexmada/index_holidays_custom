# -*- coding: utf-8 -*-
{
    'name': "Index_holidays_custom",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Dans menu Congé/Analyse, il y a un menu 'Congés restant'. On y trouve la liste de tous les employés, avec le nombres de jours de congés restant en colonne.
    """,

    'author': "Nampoina Ramarijaona, Index Consulting Madagascar",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr', 'hr_holidays'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/hr_leave_report.xml'
    ],
}
