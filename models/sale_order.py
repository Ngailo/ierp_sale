from odoo import models, fields, api

class Quotation(models.Model):
    _description = 'Sale Order'
    _inherit = 'sale.order'

    #Adding field in the inherited model
    x_ordername = fields.Char("Quotation Name")
    x_orderno = fields.Char("PO N°")
    #Relation
    purchase_id = fields.Many2one('purchase.order')
    
    
    
    @api.onchange('pricelist_id')
    def onchange_pricelist_id(self):
        """
        Update the following fields when the pricelist is changed:
        - Product unit price
        - Product price subtotal
        """

        for line in self.order_line:
            line.price_unit =  self.pricelist_id.currency_id.rate * line.product_id.lst_price
            line.price_subtotal = line.product_uom_qty * line.price_unit

    
