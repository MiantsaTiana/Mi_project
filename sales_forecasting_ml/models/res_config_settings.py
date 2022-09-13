# -*- coding: utf-8 -*-


from ast import literal_eval
from pprint import pprint
import datetime
from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools.translate import _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    def train_model(self):
        print("Training")
        begin = datetime.datetime.now()
        self.env.cr.execute("""SELECT * FROM sale_order_line""")
        # TODO ML
        response = self.env.cr.dictfetchall()
        end = datetime.datetime.now()
        print(len(response))
        pprint(response)
        print(end - begin)
