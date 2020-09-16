from odoo import models, fields, _, api
import datetime

class client_budget(models.Model):

    _name = 'budget_management.client_budget'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "budget client"

    initialAmountInMad = fields.Float(string='budget total en DH', required=True)
    initialAmountInEuros = fields.Float(string='budget total en €')
    amountLeftInMad = fields.Float(string='budget restant en DH')
    amountLeftInEuros = fields.Float(string='budget restant en €')
    amountConsumedInMad = fields.Float(string='budget consommé en DH')
    amountConsumedInEuros = fields.Float(string='budget consommé en €')
    config = fields.Many2one('budget_management.config', 'configuration')
    client = fields.Many2one('res.partner','client')
    created_at = fields.Datetime()

    @api.model
    def create(self, vals):
        vals["created_at"] = datetime.datetime.now()
        result = super(client_budget, self).create(vals)
        return result