from odoo import models, fields, api

class Company(models.Model):
    "Modifying Res Company to Include VRN"

    _inherit = 'res.company'

    x_vatno = fields.Char('VRN', required = True)
    our_partners = fields.Binary('')