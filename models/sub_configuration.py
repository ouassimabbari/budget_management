from odoo import models, fields, _, api

class subConfiguration(models.Model):
    _name = 'budget_management.sub_configuration'
    _description = "gestion de sous-configurations"

    configuration_name = fields.Char(string='Nom', required=True)
    configuration_percentage_sub_budget = fields.Float(string='Pourcentage', required=True)
    inverse_configuration = fields.Many2one('budget_management.configuration','configuration')