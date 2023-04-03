# -*- coding: utf-8 -*-
{
    'name': "Importar Facturas",

    'summary': """
        Módulo que permite importar los XMLs de las Facturas
        Electronicas de Costa Rica e incluirlas en Odoo, junto
        con la variacion de los decimales en el exchange rate,
        para que la conversión sea más precisa.
        """,

    'description': """
        Importar los XMLs de las Facturas Electronicas de Costa Rica,
        tal como si se hubieran generado desde Odoo directamente.
    """,

    'author': "Avalantec",
    'website': "http://www.avalantec.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account_accountant'],

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
}
