from odoo import fields, api, models

class Contact(models.Model):
    "Modifying Res Partner to Include VRN"

    _inherit = 'res.partner'

    x_vatno = fields.Char('VRN', required=True)