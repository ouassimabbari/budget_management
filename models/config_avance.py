from odoo import models, fields, _, api
import logging
from odoo.exceptions import ValidationError
_logger = logging.getLogger(__name__)

class config_avance(models.Model):

    _name="budget_management.avance"
    _description = "gestion de configuration des avances de campagnes"

    name = fields.Char(string='reference')
    amountInEuros = fields.Float(string="montant d'avance en euros", readonly=True, compute='_compute_amountInEuros')
    amountInMad = fields.Float(string="montant d'avance en Dhs", required=True)
    addedAt = fields.Date(string="Date d'ajout", required=True)
    campagne = fields.Many2one('budget_management.campagne','campagne', required=True)


    @api.constrains('amountInMad')
    def _check_amountInMad(self):
        names = []
        for line in self:
            lines = self.env['budget_management.avance'].search([])
            amounts = 0
            if len(lines) > 0:
                for avance_line in lines:
                    if avance_line.campagne.id == line.campagne.id:
                        amounts += avance_line.amountInMad
                
            if amounts > (line.campagne.initialAmountInMad + line.campagne.Frais):
                raise ValidationError(_("La somme des avances a dépassé le montant initial de campagne"))

        


    def _compute_amountInEuros(self):
        for avance_line in self:
            avance_line.amountInEuros = avance_line.amountInMad / avance_line.campagne.euroToMad


    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('budget_management.avance.sequence') or _('New')

        result = super(config_avance, self).create(vals)
        return result