# -*- coding: utf-8 -*-
{
    'name': "Personalizacion Inventarios Todos",

    'summary': """
       Este Modulo esta personalizado para algunas funciones propias """,

    'description': """
        por ejemplo aprobacion de transferencias, responsables de bodegas entre otras coasa
    """,

    'author': "Callhpne S.A",
    'website': "http://www.callphoneecuador.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],

    # always loaded
    'data': [
        'security/security.xml',
        'views/views.xml',
        'views/res_users.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
       # 'demo/demo.xml',
    ],
}
