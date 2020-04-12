# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    project_id = fields.Many2one(comodel_name='project.project', string='Project ID',ondelete='cascade',index=True, store=True)
    project_name = fields.Char(string = 'Project', related='project_id.name',store=True)
    

    @api.multi
    def _prepare_invoice(self):
        """
        Override the method
        """
        
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals.update({
            'project_id': self.project_id.id,
        })
        return invoice_vals




class AccountInvoice(models.Model):
    _inherit = 'account.invoice'
    
    sale_id = fields.Many2one(comodel_name='sale.order', string='Sale id',ondelete='cascade',index=True)
    project_id = fields.Many2one('project.project', string='Project ID')
    