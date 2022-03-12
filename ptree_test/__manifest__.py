# -*- coding: utf-8 -*-
{
    'name': "Ptree test module",

    'summary': """
        Esto es una prueba de creación de un nuevo modúlo en Odooo
        """,

    'description': """
        Este es un modúlo de pruebas que se instalara en Odoo para hacer pruebas de desarrollo en Odoo Version 15
    """,

    'author': "Jeerel Herrejon",
    'website': "https://ptree.com.mx/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    # Inidicamos que es una aplicacion
    'application': True,
}
