from odoo import models, fields, _, api

class configuration(models.Model):
    _name = 'budget_management.configuration'
    _description = "gestion de configurations"

    configuration_name = fields.Char(string='Nom', required=True)
    sub_configurations = fields.One2many('budget_management.sub_configuration','inverse_configuration','Sous-Configurations')