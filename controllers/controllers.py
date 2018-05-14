# -*- coding: utf-8 -*-
from odoo import http

# class MarketplaceIntegration(http.Controller):
#     @http.route('/marketplace__integration/marketplace__integration/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/marketplace__integration/marketplace__integration/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('marketplace__integration.listing', {
#             'root': '/marketplace__integration/marketplace__integration',
#             'objects': http.request.env['marketplace__integration.marketplace__integration'].search([]),
#         })

#     @http.route('/marketplace__integration/marketplace__integration/objects/<model("marketplace__integration.marketplace__integration"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('marketplace__integration.object', {
#             'object': obj
#         })