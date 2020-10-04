from odoo import models, fields, _, api
import logging
from odoo.exceptions import ValidationError
_logger = logging.getLogger(__name__)

class config_selection(models.Model):

    _name="budget_management.selection"
    _description = "gestion de configuration des budgets campagne"

    name = fields.Char(string='budget', required=True)


    @api.constrains('name')
    def _check_name(self):
        lines = self.env['budget_management.selection'].search([])
        names = []
        for line in lines:
            names.append(line.name)

        if len(names) > len(set(names)):
            raise ValidationError(_("Un nom de budget portant la même valeur saisie est déja enregistré"))