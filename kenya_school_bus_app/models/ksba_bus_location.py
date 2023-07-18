from odoo import fields, models, api
from googlemaps import Client
import polyline


class KsbaBusLocation(models.Model):
    _name = 'ksba.bus.location'
    _description = 'Bus Location'
    # _inherit = 'res.partner'
    #
    bus_id = fields.Many2one('ksba.bus', string='Bus', required=True)
    bus_locations = fields.Many2one('ksba.route',string='Bus locations')

    timestamp = fields.Datetime(default=fields.Datetime.now)

    # @api.model
    # def update_bus_location(self, bus_id, latitude, longitude):
    google_maps_api_key = fields.Many2one('ksba.route',string='Google Maps API Key')

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