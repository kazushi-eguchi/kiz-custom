# -*- coding: utf-8 -*-
{
    'name': "kiz_construction",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'kiz_ship_base', 'purchase', 'kiz_partner'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/ships.xml',
        'views/res_partner.xml',
        'views/const_files.xml',
        # 'views/const_status.xml',
        'views/const_process_line.xml',
        'views/const_product_line.xml',
        'views/const_item_line.xml',
        'views/purchase_order_line_view.xml',
        'views/purchase_order.xml',
        'views/delivery_spot.xml',
        'reports/report.xml',
        # 'reports/binding.xml',
        "security/ir.model.access.csv"
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
