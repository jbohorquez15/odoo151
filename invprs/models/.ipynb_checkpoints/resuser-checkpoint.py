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
from odoo.exceptions import UserError, ValidationError, Warning
class ResUser(models.Model):
    _inherit = 'res.users'
   
    location_ids = fields.Many2many(
        comodel_name = 'stock.location',
        relation ='location_user_rel',
        column1  ='user_id',
        column2  ='location_id',
        string   ='Ubicaciones ad Administradas',     
    )
    
    restrict_locations = fields.Boolean('Restrict Locations', readonly="1")

    stock_location_ids = fields.Many2many(
        comodel_name='stock.location',
        relation='location_security_stock_location_users',
        column1='user_id',
        column2='location_id',
        string='Stock Locations')

    default_picking_type_ids = fields.Many2many(
        comodel_name='stock.picking.type', 
        relation='stock_picking_type_users_rel',
        column1='user_id', 
        column2='picking_type_id', 
        string='Warehouse Operations')


    @api.constrains('default_picking_type_ids')
    def update_restrict(self):
        restrict_group = self.env.ref('invprs.stock_restrictions_group')
        current_group = restrict_group
        if self.stock_location_ids:
            current_group.write({'users':  [(3, self.id)]})
            self.groups_id =[(3, restrict_group.id)]
            self.restrict_locations = 0
            ##
            current_group.write({'users':  [(4, self.id)]})
            self.groups_id =[(4, restrict_group.id)]
            self.restrict_locations = 1

    @api.constrains('stock_location_ids')
    def tgl_restrict(self):
        # self.restrict_locations = not self.restrict_locations
        # res_groups = self.env['res.groups']
        restrict_group = self.env.ref('invprs.stock_restrictions_group')
        current_group = restrict_group
        if self.stock_location_ids:
            # Due to strange behaviuor, we must remove the user from the group then
            # re-add him again to get restrictions applied
            current_group.write({'users':  [(3, self.id)]})
            self.groups_id =[(3, restrict_group.id)]
            self.default_picking_type_ids = False
            self.restrict_locations = 0
            ## re-add
            # by default select all oprtations related to the selected location or its parent
            pick_types = self.env['stock.picking.type'].sudo().search(['|','|','|',
            ('default_location_src_id','in',[l.id for l in self.stock_location_ids]),
            ('default_location_src_id.location_id','in',[l.id for l in self.stock_location_ids]),
            ('default_location_dest_id','in',[l.id for l in self.stock_location_ids]),
            ('default_location_dest_id.location_id','in',[l.id for l in self.stock_location_ids]),
            ])
            current_group.write({'users':  [(4, self.id)]})
            self.groups_id =[(4, restrict_group.id)]
            self.default_picking_type_ids += pick_types
            self.restrict_locations = 1

        else:
            current_group.write({'users':  [(3, self.id)]})
            self.groups_id =[(3, restrict_group.id)]
            self.default_picking_type_ids = False
            self.restrict_locations = 0
