from odoo import models, fields, _, api
import datetime
import logging
from odoo.exceptions import ValidationError
_logger = logging.getLogger(__name__)

class budget(models.Model):

    _name = 'budget_management.budget_campagne'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "gestion de budgets"

    value = fields.Many2one('budget_management.selection','budget', required=True)
    initialAmountInMad = fields.Float(string='budget total en Dh')
    initialAmountInEuros = fields.Float(string='budget total en €', readonly=True, compute='_compute_initialAmountInEuros')
    amountLeftInMad = fields.Float(string='budget restant en Dh', readonly=True, compute='_compute_amountLeftInMad')
    amountLeftInEuros = fields.Float(string='budget restant en €', readonly=True, compute='_compute_amountLeftInEuros')
    amountConsumedInMad = fields.Float(string='budget consommé en Dh', readonly=True, compute='_compute_amountConsumedInMad')
    amountConsumedInEuros = fields.Float(string='budget consommé en €')
    startDate = fields.Date(string="Date de debut", required=True)
    endDate = fields.Date(string="Date de fin", required=True)
    inverse_budget = fields.Many2one('budget_management.campagne','campagne', required=True)
    isPercentage = fields.Selection(string='Type', selection=[('pourcentage', 'Pourcentage'), ('valeurs', 'Valeurs')], default="pourcentage")
    pourcentage = fields.Float(string='pourcentage du budget campagne')
    name = fields.Char(string='Référence de budget campagne', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))


    @api.constrains('startDate', 'endDate')
    def _check_startDate_endDate(self):
        for line in self:
            if line.startDate > line.endDate:
                raise ValidationError(_("La date de début du budget doit être ultérieure à sa date de fin"))

    @api.constrains('pourcentage')
    def _check_pourcentage(self):
        for line in self:
            if line.isPercentage == 'pourcentage':
                if line.pourcentage < 0 or line.pourcentage > 100:
                        raise ValidationError("Le pourcentage devrait être entre 0 et 100")


    def _compute_initialAmountInEuros(self):
        for budget_line in self:
            if budget_line.inverse_budget.euroToMad > 0:
                budget_line.initialAmountInEuros = budget_line.initialAmountInMad / budget_line.inverse_budget.euroToMad

    def _compute_amountLeftInMad(self):
        for budget_line in self:
            budget_line.amountLeftInMad = budget_line.initialAmountInMad - budget_line.amountConsumedInMad

    def _compute_amountLeftInEuros(self):
        for budget_line in self:
            if budget_line.inverse_budget.euroToMad > 0:
                budget_line.amountLeftInEuros = budget_line.amountLeftInMad / budget_line.inverse_budget.euroToMad


    def _compute_amountConsumedInMad(self):
        for budget_line in self:
            budget_line.amountConsumedInMad = budget_line.amountConsumedInEuros * budget_line.inverse_budget.euroToMad


    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('budget_management.budget_campagne.sequence') or _('New')

        campagne_record = self.env['budget_management.campagne'].browse(vals['inverse_budget'])

        if vals['isPercentage'] == "pourcentage":
            vals['initialAmountInMad'] = float(campagne_record.initialAmountInMad) * (float(vals['pourcentage'])/100)
        else:
            vals['pourcentage'] = (float(vals['initialAmountInMad']) * 100) / float(campagne_record.initialAmountInMad)

        result = super(budget, self).create(vals)
        return result


class SendBudgets(models.TransientModel):
    _name = 'send.budget'
    _description = 'Choisissez le budget campagne que vous voulez alimenter'

    sendTo = fields.Many2one('budget_management.budget_campagne',
                            string='Budget',
                            required=True)


    @api.onchange('sendTo')
    def onchange_sendTo(self):
        active_ids = self._context.get('active_ids', []) or []

        for record in self.env['budget_management.budget_campagne'].browse(active_ids):
            _logger.debug("client --------------------------------: %s", record.inverse_budget.client.name)
            return {'domain': {'sendTo': [('id', '!=', record.id),('inverse_budget.client.id', '=', record.inverse_budget.client.id)]}}

    def send_budget(self):
        active_ids = self._context.get('active_ids', []) or []

        for record in self.env['budget_management.budget_campagne'].browse(active_ids):
            if float(record.initialAmountInMad) >= float(record.amountConsumedInMad):

                sendToInitialAmountInMad = float(self.sendTo.initialAmountInMad) + float(record.amountLeftInMad)

                self.sendTo.write({
                    'initialAmountInMad': sendToInitialAmountInMad
                })

                New_initialAmountInMad = float(record.initialAmountInMad) - float(record.amountLeftInMad)

                record.write({
                    'initialAmountInMad': New_initialAmountInMad,
                })
            else:
                raise ValidationError("Ce budget n'est pas en mesure d'alimenter un autre budget")