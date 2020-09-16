from odoo import models, fields, _, api

class subBudget(models.Model):

    _name = 'budget_management.sub_budget'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "gestion de budgets"

    name = fields.Char(string='Nom')
    initial_Amount = fields.Float(string='budget total', required=True)
    amount_Left = fields.Float(string='budget restant')
    amount_Consumed = fields.Float(string='budget consommé')
    inverse_budget = fields.Many2one('budget_management.budget','budget')