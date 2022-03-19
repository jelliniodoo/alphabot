# -*- coding: utf-8 -*-
{
    'name': 'Alphabot Invoicing',  
    'summary': "Uso de Alphabot en Acccount Invoicing",
    'description': 'Ajustes para usar Alphabot, y conectar Odoo con las impresoras fiscales',
    'category': 'Invoicing',
    'author': 'AlphaPos',
    'website': 'http://alphapos.biz',
    "support": "info@alphapos.biz",
    "license": "Other proprietary",
    'version': '0.1.22.1.18',      
    'depends': ['base','account'],
    'data': [
        'views/account_invoice_view.xml',
        'views/res_config_settings_views.xml'
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    #'image': ['static/description/alpha_logo.png'],
}
