from odoo import models, fields, _, api

class config(models.Model):

    _name = 'budget_management.config'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "gestion de configs"

    euroToMad = fields.Float(string="1 euro en Dh", required=True)
    Frais = fields.Float(string="Frais à reduire (en DH)", required=True)