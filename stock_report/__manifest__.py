# -*- coding: utf-8 -*-
{
    'name': "stock_report",

    'summary': """
        Reporte de Inventarios""",

    'description': """
        Reporte de Inventarios
    """,

    'author': "Sursoom",
    'website': "https://www.sursoom.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Stock',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'reports/stock_report.xml',
        'reports/stock_report_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
