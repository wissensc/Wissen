from odoo import models, fields, api

class RatesTemp(models.Model):
    _name = 'rates.temp'
    _order = 'id'
    _description = 'Tasas Temporales'
    w_tasa_id = fields.Integer('Idss')
    w_tasanterior = fields.Float('Tasa Anterior')
    w_name = fields.Date()    
    w_company_id = fields.Integer('Idssss')