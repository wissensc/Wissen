# Copyright (C) 2020 Wissen MX
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, api
from odoo.osv import expression


class AccountPayment(models.Model):
    _inherit = 'account.payment'
    
    w_tasa_id = fields.Many2one('res.currency.rate', string='Fecha de Tasa')
    w_tasa = fields.Float(related = 'w_tasa_id.rate', readonly=False, string='Tasa')
    
    def rateant(self):
        temporal =  self.env['rates.temp']
        CurrencyRate = self.env['res.currency.rate']
        temporal_object = temporal.search([('w_tasa_id', '=', self.w_tasa_id.id)], limit=1, order='create_date')
        currency_object = CurrencyRate.search([('id', '=', self.w_tasa_id.id)])
        currency_object.rate = temporal_object.w_tasanterior
        temporal_object.unlink()
        return True
   
    @api.model
    def create(self, values):
        CurrencyRate = self.env['res.currency.rate']
        temporal =  self.env['rates.temp']
        currency_object = CurrencyRate.search([('id', '=', values['w_tasa_id'])])
        tasaant = currency_object.rate
        temporal.create({'w_tasa_id': currency_object.id, 'w_tasanterior': tasaant, 'w_name': currency_object.name, 'w_company_id': currency_object.company_id})
        res = super(AccountPayment, self).create(values)
        return res
      
