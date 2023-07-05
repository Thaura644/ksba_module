from odoo import fields, models

class KsbaBusLocation(models.Model):
    _name = 'ksba.bus.location'
    _description = 'Bus Location'
    # _inherit = 'res.partner'
    #
    bus_id = fields.Many2one('ksba.bus', string='Bus', required=True)
    bus_locations = fields.Float(string='Bus locations', digits=(16,6))

    timestamp = fields.Datetime(default=fields.Datetime.now)

    # @api.model
    # def update_bus_location(self, bus_id, latitude, longitude):