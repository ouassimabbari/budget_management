from odoo import models, fields, api

class contact(models.Model):
     _name = 'res.partner'
     _inherit = 'res.partner'


     campagnes = fields.One2many('budget_management.campagne','client','Campagnes')
     campagne_count = fields.Integer(compute='compute_campagnes_count')

     def get_campagnes(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Campagnes',
            'view_mode': 'tree',
            'res_model': 'budget_management.campagne',
            'domain': [('client', '=', self.id)],
            'context': "{'create': False}"
        }


     def compute_campagnes_count(self):
        for record in self:
            record.campagne_count = self.env['budget_management.campagne'].search_count(
                [('client', '=', self.id)])
