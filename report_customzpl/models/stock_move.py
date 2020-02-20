# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class StockMove(models.Model):
    _inherit = 'stock.move'
    w_num_imp = fields.Integer('Cantidad de impresiones', required=False)
