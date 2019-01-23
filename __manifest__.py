# -*- coding: utf-8 -*-
{
    'name': "iERP-Custom-Sale",

    'summary': "Extending Sales And Inventory Modules",

    'description': """
    Custom module have the following features:
               - Extend sale order to include po number and order name
               - Extend stock picking to include po number,order name
               - Extend contact to include vrn
               - Extend account invoice to include esd signature
         """,

    'author': "Invention Technologies",
    'website': "http://www.it.co.tz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Custom Module',
    'version': '11.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'stock', 'account', 'purchase', 'crm'],

    # always loaded
    'data': [
        'views/account_invoice_view.xml',
        'views/delivery_note_view.xml',
        'views/sale_order_view.xml',
        'views/res_partner_view.xml',
        'views/res_company_view.xml',
        'views/crm.xml',
    
    ],
    # only loaded in demonstration mode
    'demo': [],
    'application': True,
    'support': 'developers@it.co.tz',
}
