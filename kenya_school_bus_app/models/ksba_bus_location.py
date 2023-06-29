from odoo import fields, models

class KsbaBusLocation(models.Model):
    _name = 'ksba.bus.location'
    _description = 'Bus Location'
    # _inherit = 'res.partner'
    #
    bus = fields.Many2one('ksba.bus', string='Bus', required=True)
    location_latitude = fields.Float(string="location latitude")
    location_longitude = fields.Float(string="location longitude")
    date_time = fields.Datetime(default=fields.Datetime.now())
