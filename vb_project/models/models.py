# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    project_id = fields.Many2one(comodel_name='project.project', string='Project ID',index=True, store=True)
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
    
    sale_id = fields.Many2one(comodel_name='sale.order', string='Sale id',index=True)
    project_id = fields.Many2one('project.project', string='Project ID')


class ProjectInvoice(models.Model):
    _inherit = 'project.project'

    invoice_ids = fields.One2many('account.invoice','project_id', string='Invoices')
    payment_term_id = fields.Many2one('account.payment.term', string='Payment Terms', oldname='payment_term')
    # invoice_id = fields.Many2many("account.invoice", string='Invoices', compute="_get_invoiced", readonly=True, copy=False)


