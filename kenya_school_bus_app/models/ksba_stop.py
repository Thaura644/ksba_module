# from odoo import models, fields
#
# class KsbaStop(models.Model):
#     _name = 'ksba.stop'
#     _description = 'Stop'
#     _inherit = 'ksba.route'
#
#     name = fields.Char(required=True)
#     route_id = fields.Many2one('ksba.route', string='Route', required=True)
#     sequence =  fields.Integer()
#     latitude = fields.Float()
#     longitude = fields.Float()
#     route = fields.Many2many('ksba.route', string='Routes')
#     buses = fields.Many2many('ksba.bus', string='Buses')