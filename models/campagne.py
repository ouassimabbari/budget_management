from odoo import models, fields, _, api

class campagne(models.Model):
    _name = 'budget_management.campagne'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "gestion de campagnes"

    campagne_name = fields.Char(string='Nom', required=True)
    startDate = fields.Date(string="Date de debut", required=True)
    endDate = fields.Date(string="Date de fin", required=True)
    client = fields.Many2one('res.partner','Propriétaire de campagne')
    name_seq = fields.Char(string='Référence de campagne', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))


    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('budget_management.campagne.sequence') or _('New')
        result = super(campagne, self).create(vals)
        return result