from odoo import models, fields
from lxml import etree


class KsbaRoute(models.Model):
    _name = 'ksba.route'
    _description = 'Route'

    name = fields.Char(required=True)
    school_id = fields.Many2one('ksba.school', string='School', required=True)
    stop_ids = fields.Many2many('ksba.stop','route_ids' ,string='Stops')
    buses = fields.Many2many('ksba.bus', 'route', string='Buses')
    description = fields.Text(string='Description')
    start_location = fields.Char(string='Start Location')
    end_location = fields.Char(string='End Location')
    distance = fields.Float(string='Distance')
    duration = fields.Float(string='Duration')

    bus_ids = fields.Many2many(comodel_name='ksba.bus', string='Buses')

