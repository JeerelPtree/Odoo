# -*- coding: utf-8 -*-
# from odoo import http


# class PtreeTest(http.Controller):
#     @http.route('/ptree_test/ptree_test', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ptree_test/ptree_test/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ptree_test.listing', {
#             'root': '/ptree_test/ptree_test',
#             'objects': http.request.env['ptree_test.ptree_test'].search([]),
#         })

#     @http.route('/ptree_test/ptree_test/objects/<model("ptree_test.ptree_test"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ptree_test.object', {
#             'object': obj
#         })
