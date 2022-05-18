# -*- coding: utf-8 -*-
{
    'name': "Boletas x Pedidos",
    'description': """
           """,

    'author': "TPCO",
    'website': "http://www.tpco.com",
    'version': '14.20210208.2',

    # any module necessary for this one to work correctly

    'depends': ['sale'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/generar_boletas_views.xml',
        #'views/attributes_views.xml',
        #'views/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
