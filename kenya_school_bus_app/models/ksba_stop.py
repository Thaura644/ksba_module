from odoo import models, fields, api
from geopy.geocoders import GoogleV3

class KsbaStop(models.Model):
    _name = 'ksba.stop'
    _description = 'Stop'

    name = fields.Char(required=True)
    route_ids = fields.Many2many('ksba.route', 'stop_ids', string='Route', required=True)
    sequence = fields.Integer()
    latitude = fields.Float(string='Latitude', digits=(16,6))
    longitude = fields.Float(string='Longitude', digits=(16,6))
    from_stop_id = fields.Many2one('ksba.stop', 'From', required=True)
    to_stop_id = fields.Many2one('ksba.stop', 'To', required=True) 
    bus_ids = fields.Many2many('ksba.bus', string='Buses', relation='ksba_bus_stop_rel', column1='stop_id', column2='bus_id')

    bus_location = fields.Float(string='Bus locations', digits=(16,6))

    timestamp = fields.Datetime(default=fields.Datetime.now)

    @api.model
    def update_bus_location(self, bus_id, latitude, longitude):
        bus_location = self.search([('bus_id', '=', bus_id)], limit=1)
        if bus_location:
            bus_location.write({'location': (latitude, longitude)})

        else: 
            self.create({
                'bus_id': bus_id,
                'location': (latitude, longitude)
            })

    def fetch_live_gps():
        #your code to fetch the live gps goes here
        bus_id = ''
        latitude= ''
        longitude= ''

        bus_location_obj = self.env['ksba.stop']
        bus_location_obj.update_bus_location(bus_id, latitude, longitude)




    # def get_geolocation(address):
    #     geolocator = GoogleV3(api_key='YOUR_API-KEY')
    #     location = geolocator.geocode(address)
    #     if  location: 
    #         latitude = location.latitude
    #         longitude = location.longitude



    # def update_latitude(self, latitude):
    #     self.ensure_one()
    #     self.latitude = latitude

   