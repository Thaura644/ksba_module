from odoo import models, fields, api
from lxml import etree
from googlemaps import Client
import math
import polyline

class KsbaRoute(models.Model):
    _name = 'ksba.route'
    _description = 'Route'

    name = fields.Char(required=True)
    stop_ids = fields.Many2many('ksba.stop', string='Stops')
    cost = fields.Float('Cost')
    buses = fields.Many2many('ksba.bus', 'route', string='Buses')
    description = fields.Text(string='Description')
    start_location = fields.Float(string='Start Location',digits=(16,6) )
    end_location = fields.Float(string='End Location',digits=(16,6))
    start_time = fields.Float('Start Time', required=True)
    end_time = fields.Float('End Time', required=True)
    student_ids = fields.Many2many('ksba.school', string='Student(s)')

    latitude = fields.Float(string='Latitude', digits=(16, 6))
    longitude = fields.Float(string='Longitude', digits=(16, 6))
    bus_locations = fields.Many2one('ksba.bus.location', string='Bus locations')

    distance = fields.Float(string='Distance', compute='_compute_distance', store=True)
    duration = fields.Float(string='Duration', compute='_compute_duration', store=True)

    bus_ids = fields.Many2many('ksba.bus', string='Buses')

    google_maps_api_key = fields.Many2one(string='Google Maps API Key')
    map_url = fields.Char(string='Map URL', compute='_compute_map_url')

    @api.depends('bus_locations', 'google_maps_api_key')
    def _compute_map_url(self):
        gmaps = Client(key=self.google_maps_api_key)
        for location in self:
            encoded_polyline = polyline.encode([
                (location.bus_locations, 0.0),  # Add other coordinates here if needed
            ])
            map_url = gmaps.static_map(
                encoded_polyline,
                size=(400, 400),
                zoom=15
            )
            location.map_url = map_url

    