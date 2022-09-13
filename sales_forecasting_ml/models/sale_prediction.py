# -*- coding: utf-8 -*-


from datetime import timedelta

from odoo import api, fields, models, _
from ..fields import JobSerialized


class SaleOrderLinePredicted(models.Model):
    _name = 'sale.order.line.predicted'
    _description = "Machine learning model"

    prediction_date = fields.Datetime(string="Prediction date")
    dataset = JobSerialized(string="Dataset (serialized)", base_type=list)
    dataset_model = fields.Binary(string="Model file")
