from odoo import models, fields,api
import math

class KsbaRoute(models.Model):
    _name = 'ksba.route'
    _description = 'Route'

    name = fields.Char(required=True)
    stop_ids = fields.Many2many('ksba.stop','route_ids' ,string='Stops')
    buses = fields.Many2many('ksba.bus', 'route', string='Buses')
    description = fields.Text(string='Description')
    start_location = fields.Float(string='Start Location')
    end_location = fields.Float(string='End Location')
    distance = fields.Float(string='Distance')
    duration = fields.Float(string='Duration')

    bus_ids = fields.Many2many(comodel_name='ksba.bus', string='Buses')
    
    @api.depends('start_location', 'end_location')
    def _compute_distance(self):
        for route in self:
            if route.start_location and route.end_location:
                lat1 = math.radians(route.start_location)
                lon1 = math.radians(0)  # Assuming longitude is 0 for simplicity
                lat2 = math.radians(route.end_location)
                lon2 = math.radians(0)  # Assuming longitude is 0 for simplicity

                radius = 6371  # Earth radius in kilometers
                delta_lat = lat2 - lat1
                delta_lon = lon2 - lon1

                a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon / 2) ** 2
                c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
                distance_km = radius * c

                route.distance = distance_km