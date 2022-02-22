# -*- coding: utf-8 -*-
{
    'name': "kiz_ship_base",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Kazushi Eguchi(Enzantrades Inc,)",
    'website': "https://github.com/kazushi-eguchi/kiz_ship_base",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm', 'kiz_partner'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        "views/ships.xml",
        "views/ships_type.xml",
        "views/lead.xml",
        "security/ir.model.access.csv"
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
