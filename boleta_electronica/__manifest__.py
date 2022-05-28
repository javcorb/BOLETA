# -*- coding: utf-8 -*-
{
    'name': "Boleta Electrónica",
    'description': """
           """,

    'author': "TPCO",
    'website': "http://www.tpco.com",
    'version': '14.20210208.2',

    # any module necessary for this one to work correctly

    'depends': ['sale', 'base_setup'],

    # always loaded
    'data': [
          # 'views/boleta_electronica_views.xml',
          # 'views/boleta_electronica_assets.xml',
          'report/templates/boleta_electronica_reports.xml',
          'report/templates/boleta_electronica_report_view.xml',

          # 'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
