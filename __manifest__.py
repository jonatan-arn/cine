# -*- coding: utf-8 -*-
{
    'name': "cine",

    'summary': """
       Aplicacion de gestion de un cine""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Jonatan Arnandis Alfonso",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/cine_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/peliculas_view.xml',
        'views/horario_view.xml',
        'views/salas_view.xml',
        'views/venta_snack_view.xml',
        'views/empleados_view.xml',
        'views/snacks_view.xml',
        'views/menu_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}
