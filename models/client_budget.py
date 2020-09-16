from odoo import models, fields, _, api
import datetime
import json
import logging
_logger = logging.getLogger(__name__)

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
        _logger.debug("this is the vals ----------------------- %s",vals)
        config_id = vals['config']
        _logger.debug("this is the config_id ----------------------- %s",config_id)
        config_record = self.env['budget_management.config'].browse(vals['config'])
        _logger.debug("this is the config ----------------------- %s",config_record)
        _logger.debug("this is the frais ----------------------- %s",config_record.Frais)
        vals["created_at"] = datetime.datetime.now()
        result = super(client_budget, self).create(vals)
        return result