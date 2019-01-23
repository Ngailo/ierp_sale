from odoo import models, fields, api


class Delivery(models.Model):
   
    _inherit = 'stock.picking'

    sale_id = fields.Many2one('sale.order', '', store=True)
    x_orderno = fields.Char('PO N°', compute="get_no")
    x_ordername = fields.Char('Quotation Name', compute="get_name")
    
    
    
    
    @api.one
    @api.depends('origin')
    def get_name(self):
        for rec in self.env['sale.order'].search([('name', '=', self.origin)])[0]:
            self['x_ordername'] = rec.x_ordername
    
    
    @api.one
    @api.depends('origin')
    def get_no(self):
        for rec in self.env['sale.order'].search([('name', '=', self.origin)])[0]:
            self['x_orderno'] = rec.x_orderno

   