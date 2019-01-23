from odoo import models, fields, api

class Quotation(models.Model):
    
    _inherit = 'sale.order'

    #Adding field in the inherited model
    x_ordername = fields.Char("Quotation Name")
    x_orderno = fields.Char("PO N°")
    requester_name = fields.Char("Requester Name")
   
    #Relation
    purchase_id = fields.Many2one('purchase.order')
    
    
    


    
