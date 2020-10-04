from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class contact(models.Model):
     _inherit = 'res.partner'


     campagnes = fields.One2many('budget_management.campagne','client','Campagnes')
     campagne_count = fields.Integer(compute='compute_campagnes_count')
<<<<<<< HEAD
     #budget = fields.Many2one('budget_management.client_budget', 'budget')
     #client_budget_selected = fields.Boolean(default=False)


     #def write(self, vals):
        #_logger.debug("this is self:------------------------- %s", self)
        #_logger.debug("this is vals:------------------------- %s", vals)
        #result = super(contact, self).write(vals)
        #return result

     #@api.onchange('campagnes')
     #def onchange_campagnes(self):
        #_logger.debug("this is self:------------------------- %s", self)
        #pos = -1
        #for line in self.campagnes:
            #pos += 1
            #if pos == len(self.campagnes) - 1:
                #_logger.debug("this is campagnes:------------------------- %s", line.campagne_name)
        #_logger.debug("this is budget:------------------------- %s", self.budget)

    #  @api.onchange('budget')
    #  def onchange_budget(self):
    #     if self.budget:
    #         self.client_budget_selected = True
    #     else:
    #         self.client_budget_selected = False
=======
>>>>>>> 22a8b6fff1050f5ff11791934ffeb468293f6436

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

    
