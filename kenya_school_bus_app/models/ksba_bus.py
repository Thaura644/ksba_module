from odoo import models, fields

class KsbaBus(models.Model):
    _name = 'ksba.bus'
    _description = 'Bus'

    name= fields.Char(string="Bus Name", required=True)
    bus_id = fields.Char(string="plate_number",required=True)
    vehicle_id = fields.Many2one('ksba.bus', 'Vehicle', required=True)
    school_id = fields.Many2one('ksba.school', string='School', required=True)
    driver_ids = fields.Many2one('ksba.partners', string='Driver')
    capacity = fields.Integer(required=True)
    route = fields.Many2many('ksba.route', string='Route')
    bus_locations = fields.Float(string='Bus locations', digits=(16,6))
    current_location = fields.Float(string='current location', digits=(16,6))
    latitude = fields.Float(string='Latitude', digits=(16,6))
    longitude = fields.Float(string='Longitude', digits=(16,6))
    child_ids = fields.One2many(
    'ksba.child',
        'bus_id',
        string='Children'
    )
    stop_ids = fields.Many2one('ksba.stop',string="Stops")