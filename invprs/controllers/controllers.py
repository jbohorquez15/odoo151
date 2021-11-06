# -*- coding: utf-8 -*-
# from odoo import http


# class InventarioPrs(http.Controller):
#     @http.route('/inventario_prs/inventario_prs/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inventario_prs/inventario_prs/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inventario_prs.listing', {
#             'root': '/inventario_prs/inventario_prs',
#             'objects': http.request.env['inventario_prs.inventario_prs'].search([]),
#         })

#     @http.route('/inventario_prs/inventario_prs/objects/<model("inventario_prs.inventario_prs"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inventario_prs.object', {
#             'object': obj
#         })
