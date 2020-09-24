from odoo import models, fields, _, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class campagne(models.Model):
    _name = 'budget_management.campagne'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "gestion de campagnes"

    campagne_name = fields.Char(string='Nom', required=True)
    startDate = fields.Date(string="Date de debut", required=True)
    endDate = fields.Date(string="Date de fin", required=True)
    client = fields.Many2one('res.partner','Propriétaire de campagne', required=True)
    initialAmountInMad = fields.Float(string='budget initial en Dh', required=True)
    initialAmountInEuros = fields.Float(string='budget initial en Euros', readonly=True)
    amountLeftInMad = fields.Float(string='budget restant en Dh', readonly=True)
    amountLeftInEuros = fields.Float(string='budget restant en Euros', readonly=True)
    amountConsumedInMad = fields.Float(string='budget consommé en Dh', readonly=True)
    amountConsumedInEuros = fields.Float(string='budget consommé en Euros')
    Frais = fields.Float(string='Frais à résuire en Dh', required=True)
    EurosToMad = fields.Float(string='1 Euro en Dhs', required=True)
    name_seq = fields.Char(string='Référence de campagne', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))


    @api.model
    def create(self, vals):
        _logger.debug("this is vals:------------------------- %s", vals)
        print(vals)
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('budget_management.campagne.sequence') or _('New')
        
        #vals['initialAmountInMad'] = float(vals['initialAmountInMad']) - float(vals['Frais'])
        #vals['initialAmountInEuros'] = float(vals['initialAmountInMad']) / float(vals['EurosToMad'])
        
        #if float(vals['amountConsumedInMad']) > float(vals['initialAmountInMad']):
            #raise ValidationError("Le budget consommé ne peut pas être supérieur au budget initial")
        #else:
            #vals['amountConsumedInEuros'] = float(vals['amountConsumedInMad']) / float(vals['EurosToMad'])
            #vals['amountLeftInMad'] = float(vals['initialAmountInMad']) - float(vals['amountConsumedInMad'])
            #vals['amountLeftInEuros'] = float(vals['initialAmountInEuros']) - float(vals['amountConsumedInEuros'])

        result = super(campagne, self).create(vals)
        return result