# -*- coding: utf-8 -*-
from odoo import http

# class IerpSale(http.Controller):
#     @http.route('/ierp_sale/ierp_sale/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ierp_sale/ierp_sale/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ierp_sale.listing', {
#             'root': '/ierp_sale/ierp_sale',
#             'objects': http.request.env['ierp_sale.ierp_sale'].search([]),
#         })

#     @http.route('/ierp_sale/ierp_sale/objects/<model("ierp_sale.ierp_sale"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ierp_sale.object', {
#             'object': obj
#         })