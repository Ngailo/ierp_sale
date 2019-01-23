from odoo import models, fields, api


class Invoice(models.Model):
    
    _inherit = 'account.invoice'

    @api.one
    @api.depends('origin')
    def get_requester_name(self):
        for rec in self.env['sale.order'].search([('name', '=', self.origin)]):
            self['requester_name'] = rec.requester_name
    
    @api.one
    @api.depends('origin')
    def get_no(self):
        for rec in self.env['sale.order'].search([('name', '=', self.origin)]):
            self['x_orderno'] = rec.x_orderno
  
    @api.one
    @api.depends('origin')
    def get_name(self):
        for rec in self.env['sale.order'].search([('name', '=', self.origin)]):
            self['x_ordername'] = rec.x_ordername
    
 
    @api.one
    @api.depends('partner_id')
    def get_vrn_no(self):
        for rec in self.partner_id:
            self['x_vatno'] = rec.x_vatno



    x_vatsignature = fields.Char('ESD Signature')
    sale_id = fields.Many2one('sale.order')
    x_ordername = fields.Char('Quote Name', compute='get_name')
    x_orderno = fields.Char('PO N°', compute='get_no')
    requester_name = fields.Char('Requester Name', compute='get_requester_name')
    x_vatno = fields.Char('VAT No', compute='get_vrn_no', required=True)
