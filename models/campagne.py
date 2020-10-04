from odoo import models, fields, _, api
import datetime
from odoo.exceptions import ValidationError
from odoo.exceptions import Warning
import json
import logging
_logger = logging.getLogger(__name__)

class campagne(models.Model):
    _name = 'budget_management.campagne'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "gestion de campagnes"

    state = fields.Selection([
        ('brouillon', 'Brouillon'),
        ('validé', 'Validé'),
        ('actif', 'Actif'),
        ('intérrompu', 'Intérrompu'),
        ('arrété', 'Arrété'),
        ('terminé', 'Terminé'),
        ('annulé', 'Annulé')], string='Status', readonly=True, copy=False, default='brouillon')
    campagne_name = fields.Char(string='Nom', required=True)
    startDate = fields.Date(string="Date de debut", required=True)
    endDate = fields.Date(string="Date de fin", required=True)
    client = fields.Many2one('res.partner','Propriétaire de campagne', required=True)
    initialAmountInMad = fields.Float(string='budget initial en Dh', required=True)
    initialAmountInMadMinusCharges = fields.Float(string='budget initial en Dh sans frais', readonly=True, compute='_compute_initialAmountInMadMinusCharges')
    initialAmountInEuros = fields.Float(string='budget initial en Euros', readonly=True, compute='_compute_initialAmountInEuros')
    initialAmountInEurosMinusCharges = fields.Float(string='budget initial en Euros sans frais', readonly=True, compute='_compute_initialAmountInEurosMinusCharges')
    amountLeftInMad = fields.Float(string='budget restant en Dh', readonly=True, compute='_compute_amountLeftInMad')
    amountLeftInEuros = fields.Float(string='budget restant en Euros', readonly=True, compute='_compute_amountLeftInEuros')
    amountConsumedInMad = fields.Float(string='budget consommé en Dh', readonly=True, compute='_compute_amountConsumedInMad')
    amountConsumedInEuros = fields.Float(string='budget consommé en Euros', readonly=True, compute='_compute_amountConsumedInEuros')
    euroToMad = fields.Float(string="1 euro en Dh", required=True)
    Frais = fields.Float(string="Frais à reduire (en DH)", required=True)
    budgets = fields.One2many('budget_management.budget_campagne','inverse_budget','budgets')
    avances = fields.One2many('budget_management.avance','campagne','avances')
    budget_count = fields.Integer(compute='compute_budgets_count')
    avance_count = fields.Integer(compute='compute_avances_count')
    name = fields.Char(string='Référence de campagne', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    availableBudgetInMad = fields.Float(string="budget disponible en Dh", readonly=True, compute='_compute_availableBudgetInMad')
    availableBudgetInEuros = fields.Float(string="budget disponible en Euros", readonly=True, compute='_compute_availableBudgetInEuros')



    def action_interrupt(self):
        for line in self:
            line.state = 'intérrompu'


    def action_stop(self):
        for line in self:
            line.state = 'arrété'


    def action_end(self):
        for line in self:
            line.state = 'terminé'

    def action_activate(self):
        for line in self:
            line.state = 'actif'

    def action_validate(self):
        for line in self:
            line.state = 'validé'

    def action_cancel(self):
        for line in self:
            line.state = 'annulé'



    @api.constrains('startDate', 'endDate')
    def _check_startDate_endDate(self):
        for line in self:
            if line.startDate > line.endDate:
                raise ValidationError(_("La date de fin de campagne doit être ultérieure à celle du début"))


    @api.constrains('startDate', 'budgets')
    def _check_startDate_budgetStartDate(self):
        for campagne_line in self:
            for budget_line in self.budgets:
                if campagne_line.startDate > budget_line.startDate:
                    raise ValidationError(_("La date de début de campagne doit être antérieure à celle du début de ses budgets"))


    @api.constrains('endDate', 'budgets')
    def _check_endDate_budgetEndDate(self):
        for campagne_line in self:
            for budget_line in self.budgets:
                if campagne_line.endDate < budget_line.endDate:
                    raise ValidationError(_("La date de fin de campagne doit être ultérieure à celle de fin de ses budgets"))


    @api.constrains('initialAmountInMad', 'Frais')
    def _check_initialAmountInMad_Frais(self):
        for line in self:
            if line.initialAmountInMad < line.Frais:
                raise ValidationError(_("Le montant des frais à réduire doit être inférieur au montant initial de campagne"))

    @api.constrains('initialAmountInMad')
    def _check_initialAmountInMad_budgets(self):
        for campagne_line in self:
            initialAmounts = 0
            if len(self.budgets) > 0:
                for budget_line in self.budgets:
                    initialAmounts += budget_line.initialAmountInMad
                if campagne_line.initialAmountInMad < initialAmounts:
                    raise ValidationError(_("Le montant initial de campagne n'est pas suffisant pour alimenter les budgets saisis"))

    @api.constrains('budgets')
    def _check_budgets_values(self):
        budgetValues = []
        if len(self.budgets) > 0:
            for line in self.budgets:
                budgetValues.append(line.value.name)

            if len(budgetValues) != len(set(budgetValues)):
                raise ValidationError("Vous avez saisi un budget dupliqué")

    @api.constrains('budgets')
    def _check_budgets_amountsConsumed(self):
        amountsConsumedInEuros= 0
        if len(self.budgets) > 0:
            for budget_line in self.budgets:
                amountsConsumedInEuros += budget_line.amountConsumedInEuros
            for campagne_line in self:
                if amountsConsumedInEuros > (campagne_line.initialAmountInMad / campagne_line.euroToMad):
                    raise ValidationError("Le budget restant de campagne n'est pas alimenté suffisament pour couvrir le budget consommé saisi")

    @api.constrains('budgets')
    def _check_budgets_initialAmounts(self):
        initialAmountsInEuros= 0
        if len(self.budgets) > 0:
            for budget_line in self.budgets:
                initialAmountsInEuros += budget_line.initialAmountInEuros
            for campagne_line in self:
                if initialAmountsInEuros > (campagne_line.initialAmountInMad / campagne_line.euroToMad):
                    raise ValidationError("Le budget initial de campagne n'est pas alimenté suffisament pour couvrir les budgets saisis")

    def _compute_initialAmountInEuros(self):
        for line in self:
            if line.euroToMad > 0:
                line.initialAmountInEuros = line.initialAmountInMad / line.euroToMad

    def _compute_initialAmountInEurosMinusCharges(self):
        for line in self:
            if line.euroToMad > 0:
                line.initialAmountInEurosMinusCharges = line.initialAmountInEuros + (line.Frais / line.euroToMad)

    def _compute_initialAmountInMadMinusCharges(self):
        for line in self:
            if line.euroToMad > 0:
                line.initialAmountInMadMinusCharges = line.initialAmountInMad + line.Frais

    def _compute_amountLeftInMad(self):
        for line in self:
            if line.euroToMad > 0:
                line.amountLeftInMad = line.initialAmountInMad - line.amountConsumedInMad


    def _compute_amountConsumedInMad(self):
        for campagne_line in self:
            if len(campagne_line.budgets) > 0:
                amountsConsumed = 0
                for budget_line in campagne_line.budgets:
                    amountsConsumed += budget_line.amountConsumedInMad
                campagne_line.amountConsumedInMad = amountsConsumed
            else:
                campagne_line.amountConsumedInMad = 0

    def _compute_amountConsumedInEuros(self):
        for campagne_line in self:
            if campagne_line.euroToMad > 0:
                campagne_line.amountConsumedInEuros = campagne_line.amountConsumedInMad / campagne_line.euroToMad

    def _compute_amountLeftInEuros(self):
        for campagne_line in self:
            if campagne_line.euroToMad > 0:
                campagne_line.amountLeftInEuros = campagne_line.amountLeftInMad / campagne_line.euroToMad


    def _compute_availableBudgetInMad(self):
        for campagne_line in self:
            if len(self.budgets) > 0:
                initialAmounts = 0
                for budget_line in self.budgets:
                    initialAmounts += budget_line.initialAmountInMad

                campagne_line.availableBudgetInMad = campagne_line.initialAmountInMad - initialAmounts
            else:
                campagne_line.availableBudgetInMad = campagne_line.initialAmountInMad


    def _compute_availableBudgetInEuros(self):
        for campagne_line in self:
            campagne_line.availableBudgetInEuros = campagne_line.availableBudgetInMad / campagne_line.euroToMad


    @api.onchange('budgets')
    def _onchange_budget(self):
        for line in self:
            avanceAmounts = 0
            amountsConsumed = 0
            if len(line.avances) > 0:
                for avance_line in line.avances:
                    avanceAmounts += avance_line.amountInEuros
                for budget_line in line.budgets:
                    amountsConsumed += budget_line.amountConsumedInEuros
                if amountsConsumed > avanceAmounts:
                    amountToShow = (amountsConsumed - avanceAmounts) * line.euroToMad
                    return {
                        'warning': {
                            'title': _('Avance dépassé.'),
                            'message': _("Le montant consommé de campagne à dépassé le montant des avance de %d Dhs" % amountToShow)
                        }
                    }
                elif amountsConsumed > (avanceAmounts * 0.8) and amountsConsumed < avanceAmounts:
                    amountToShow = (avanceAmounts - amountsConsumed) * line.euroToMad
                    return {
                        'warning': {
                            'title': _('Attention.'),
                            'message': _("Votre consommation s'approche du montant d'avance  de %d Dhs" % amountToShow)
                        }
                    }

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('budget_management.campagne.sequence') or _('New')

        vals['initialAmountInMad'] = float(vals['initialAmountInMad']) - float(vals['Frais'])

        result = super(campagne, self).create(vals)
        return result

    def write(self, vals):
        if 'Frais' in vals.keys() and 'initialAmountInMad' in vals.keys():
            vals['initialAmountInMad'] = float(vals['initialAmountInMad']) - float(vals['Frais'])
        elif 'Frais' in vals.keys() and 'initialAmountInMad' not in vals.keys():
            vals['initialAmountInMad'] = self.initialAmountInMad + self.Frais - float(vals['Frais'])
        elif 'initialAmountInMad' in vals.keys() and 'Frais' not in vals.keys():
            vals['initialAmountInMad'] = float(vals['initialAmountInMad']) - self.Frais

        result = super(campagne, self).write(vals)
        return result


    @api.onchange('budgets')
    def onchange_budgets(self):
        _logger.debug("self--------------------------------: %s", self)

    
    def get_budgets(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Budgets',
            'view_mode': 'tree,form',
            'res_model': 'budget_management.budget_campagne',
            'domain': [('inverse_budget', '=', self.id)],
            'context': "{'create': False}"
        }


    def compute_budgets_count(self):
        for record in self:
            record.budget_count = self.env['budget_management.budget_campagne'].search_count(
                [('inverse_budget', '=', self.id)])



    def get_avances(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Avances',
            'view_mode': 'tree,form',
            'res_model': 'budget_management.avance',
            'domain': [('campagne', '=', self.id)],
            'context': "{'create': False}"
        }

    def compute_avances_count(self):
        for record in self:
            record.avance_count = self.env['budget_management.avance'].search_count(
                [('campagne', '=', self.id)])
