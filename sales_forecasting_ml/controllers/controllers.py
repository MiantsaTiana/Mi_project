# -*- coding: utf-8 -*-
# from odoo import http


# class SalesForecastingMl(http.Controller):
#     @http.route('/sales_forecasting_ml/sales_forecasting_ml/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_forecasting_ml/sales_forecasting_ml/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_forecasting_ml.listing', {
#             'root': '/sales_forecasting_ml/sales_forecasting_ml',
#             'objects': http.request.env['sales_forecasting_ml.sales_forecasting_ml'].search([]),
#         })

#     @http.route('/sales_forecasting_ml/sales_forecasting_ml/objects/<model("sales_forecasting_ml.sales_forecasting_ml"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_forecasting_ml.object', {
#             'object': obj
#         })
