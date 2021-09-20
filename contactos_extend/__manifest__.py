# -*- coding: utf-8 -*-
{
    'name': "contactos_extend",

    'summary': """
        Extendemos el modulo de Contactos""",

    'description': """
        Para agregar los datos de los Pacientes...
    """,

    'author': "Sursoom",
    'website': "https://www.sursoom.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/simple.xml',
        'reports/detallado.xml'
        'reports/detallado_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
