from odoo import models, fields, _, api
from odoo.exceptions import ValidationError
import datetime
import json
import logging
_logger = logging.getLogger(__name__)

class client_budget(models.Model):

    _name = 'budget_management.client_budget'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "budget client"

    initialAmountInMad = fields.Float(string='budget total en DH', required=True)
    initialAmountInEuros = fields.Float(string='budget total en €', readonly=True)
    amountLeftInMad = fields.Float(string='budget restant en DH', readonly=True)
    amountLeftInEuros = fields.Float(string='budget restant en €')
    amountConsumedInMad = fields.Float(string='budget consommé en DH', readonly=True)
    amountConsumedInEuros = fields.Float(string='budget consommé en €', readonly=True)
    config = fields.Many2one('budget_management.config', 'configuration', required=True)
    created_at = fields.Datetime(string="crée le : ", readonly=True)

    @api.model
    def create(self, vals):
        config_record = self.env['budget_management.config'].browse(vals['config'])
        vals["initialAmountInMad"] = float(vals["initialAmountInMad"]) - float(config_record.Frais)
        vals["initialAmountInEuros"] = float(vals["initialAmountInMad"]) / float(config_record.euroToMad)
        vals["amountLeftInMad"] = vals["initialAmountInMad"]
        vals["amountLeftInEuros"] = vals["initialAmountInEuros"]
        vals["created_at"] = datetime.datetime.now()
        result = super(client_budget, self).create(vals)
        return result


    def write(self, vals):
        _logger.debug("this is self:------------------------- %s", self)
        if 'config' in vals.keys():
            config_record = self.env['budget_management.config'].browse(vals['config'])
        else:
            config_record = self.config

        if 'initialAmountInMad' in vals.keys():
            New_initialAmountInMad = float(vals["initialAmountInMad"]) - float(config_record.Frais)
            New_initialAmountInEuros = float(vals["initialAmountInMad"]) / float(config_record.euroToMad)
        else:
            New_initialAmountInMad = self.initialAmountInMad
            New_initialAmountInEuros = self.initialAmountInEuros

        if 'amountLeftInEuros' in vals.keys():
            New_amountLeftInEuros = float(vals['amountLeftInEuros'])
        else:
            New_amountLeftInEuros = float(self.amountLeftInEuros)

        if New_amountLeftInEuros > New_initialAmountInEuros:
            raise ValidationError("Le budget restant ne peut pas être supérieur au budget initial")
        else:
            New_amountLeftInMad = float(New_amountLeftInEuros) * float(config_record.euroToMad)
            New_amountConsumedInEuros = float(New_initialAmountInEuros) - float(New_amountLeftInEuros)
            New_amountConsumedInMad = float(New_amountConsumedInEuros) * float(config_record.euroToMad)
            result = super(client_budget, self).write({
                'initialAmountInMad': New_initialAmountInMad,
                'initialAmountInEuros': New_initialAmountInEuros,
                'amountLeftInMad': New_amountLeftInMad,
                'amountLeftInEuros': New_amountLeftInEuros,
                'amountConsumedInMad': New_amountConsumedInMad,
                'amountConsumedInEuros': New_amountConsumedInEuros,
                'config': config_record
            })

        return result