from odoo import models, fields, _, api

class budget(models.Model):

    _name = 'budget_management.budget'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "gestion de budgets"

    budget_name = fields.Char(string='Nom')
    initialAmount = fields.Float(string='budget total', required=True)
    amountLeft = fields.Float(string='budget restant')
    amountConsumed = fields.Float(string='budget consommé')
    configuration = fields.Many2one('budget_management.configuration','configuration')
    sub_budgets = fields.One2many('budget_management.sub_budget','inverse_budget','Sous budgets')
    client = fields.Many2one('res.partner','client')