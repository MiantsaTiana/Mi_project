# -*- coding: utf-8 -*-
{
    'name': "Sales forecasting ML",

    'summary': """
    Sales forecasting using Machine Learning
       """,

    'description': """
       Sales forecasting ML
    """,

    'author': "RAZAKAMANANTSOA Miantsa Tiana",
    # 'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales/Forecast',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_management'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # Views
        'views/sale_views.xml',
        'views/res_config_settings_views.xml',

        'report/sale_prediction_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
