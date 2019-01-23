from odoo import models, fields, api


class Invoice(models.Model):
    
    _inherit = 'account.invoice'
    
    @api.one
    @api.depends('origin')
    def get_no(self):
        for rec in self.env['sale.order'].search([('name', '=', self.origin)])[0]:
            self['x_orderno'] = rec.x_orderno
  
    @api.one
    @api.depends('origin')
    def get_name(self):
        for rec in self.env['sale.order'].search([('name', '=', self.origin)])[0]:
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
    x_vatno = fields.Char('VAT No', compute='get_vrn_no', required=True)