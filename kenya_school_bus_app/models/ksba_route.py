from odoo import models, fields, api
import math

class KsbaRoute(models.Model):
    _name = 'ksba.route'
    _description = 'Route'

    name = fields.Char(required=True)
    stop_ids = fields.Many2many('ksba.stop', 'route_ids', string='Stops')
    description = fields.Text(string='Description')
    start_location_latitude = fields.Float(string='Start Location Latitude')
    start_location_longitude = fields.Float(string='Start Location Longitude')
    end_location_latitude = fields.Float(string='End Location Latitude')
    end_location_longitude = fields.Float(string='End Location Longitude')

    bus_ids = fields.Many2many(comodel_name='ksba.bus', string='Buses')
    distance = fields.Float(string='Distance', compute='_compute_distance')

    @api.depends('start_location_latitude', 'start_location_longitude', 'end_location_latitude', 'end_location_longitude')
    def _compute_distance(self):
        for route in self:
            if route.start_location_latitude and route.start_location_longitude and route.end_location_latitude and route.end_location_longitude:
                lat1 = math.radians(route.start_location_latitude)
                lon1 = math.radians(route.start_location_longitude)
                lat2 = math.radians(route.end_location_latitude)
                lon2 = math.radians(route.end_location_longitude)

                # Haversine formula
                dlon = lon2 - lon1
                dlat = lat2 - lat1
                a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
                c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
                distance = 6371 * c  # Earth's radius in kilometers
                route.distance = distance
            else:
                route.distance = 0.0
