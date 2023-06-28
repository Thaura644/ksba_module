from odoo import models, fields

class KsbaBus(models.Model):
    _name = 'ksba.bus'
    _description = 'Bus'

    plate_number = fields.Char(required=True)
    school_id = fields.Many2one('ksba.school', string='School', required=True)
    driver_id = fields.Many2one('ksba.partners', string='Driver')
    capacity = fields.Integer(required=True)
    route = fields.Many2many('ksba.route', string='Route')
    bus_locations = fields.One2many('ksba.bus.location', 'bus', string='Bus locations')
    current_location = fields.Float(string="current_location")
    child_ids = fields.One2many(
    'ksba.child',
        'bus_id',
        string='Children'
    )
    stop_ids = fields.Many2one('ksba.stop',string="Stops")