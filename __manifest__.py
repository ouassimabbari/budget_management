# -*- coding: utf-8 -*-
{
    'name': "budget_management",

    'summary': """
        module de gestion de budget de campagnes publicitaires""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Novway",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/client.xml',
        'views/campagne.xml',
        'views/budget.xml',
        'views/client_budget.xml',
        'views/configuration.xml',
        'views/config.xml',
        'views/sub_configuration.xml',
        'views/sub_budget.xml',
        'data/sequence.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}