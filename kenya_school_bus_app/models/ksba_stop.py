from odoo import models, fields

class KsbaStop(models.Model):
    _name = 'ksba.stop'
    _description = 'Stop'
    # _inherit = 'ksba.route'

    name = fields.Char(required=True)
    route_ids = fields.Many2many('ksba.route','stop_ids',string='Route', required=True)
    sequence =  fields.Integer()
    latitude = fields.Float()
    longitude = fields.Float()
    bus = fields.One2many('ksba.bus','stop_ids', string='Buses')