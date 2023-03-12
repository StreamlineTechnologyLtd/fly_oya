# -*- coding: utf-8 -*-
{
    'name': "account_oya",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account', 'master_oya', 'account_asset', 'sale', 'purchase', 'hr_expense'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/account_move_line.xml',
        'views/account_asset.xml',
        'views/sale_order.xml',
        'views/purchase_order.xml',
        'views/hr_expense.xml',
        
    ],
    'assets': {
        'web.assets_backend': [
            ('replace', 'account/static/src/js/legacy_account_selection.js',
             'account_oya/static/src/js/legacy_account_selection.js'), 
            ('replace', 'account/static/src/components/account_type_selection/account_type_selection.js',
             'account_oya/static/src/components/account_type_selection/account_type_selection.js'),
        ],},
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
