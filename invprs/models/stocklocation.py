# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class inventario_prs(models.Model):
#     _name = 'inventario_prs.inventario_prs'
#     _description = 'inventario_prs.inventario_prs'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
class StockLocation(models.Model):
    _inherit = 'stock.location'
   
    users_ids = fields.Many2many(
        comodel_name = 'res.users',
        relation ='location_user_rel',
        column1  ='location_id',
        column2  ='user_id',
        string   ='Usuarios Responsables',     
    )