# -*- coding: utf-8 -*-


from datetime import timedelta

from odoo import api, fields, models, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
