# -*- coding: utf-8 -*-
# from odoo import http


# class Pconuba(http.Controller):
#     @http.route('/pconuba/pconuba', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pconuba/pconuba/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pconuba.listing', {
#             'root': '/pconuba/pconuba',
#             'objects': http.request.env['pconuba.pconuba'].search([]),
#         })

#     @http.route('/pconuba/pconuba/objects/<model("pconuba.pconuba"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pconuba.object', {
#             'object': obj
#         })

