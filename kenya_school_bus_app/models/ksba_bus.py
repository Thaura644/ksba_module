# from odoo import models, fields
#
# class KsbaBus(models.Model):
#     _name = 'ksba.bus'
#     _description = 'Bus'
#     _inherit = 'ksba.school'
#
#     name = fields.Char(required=True)
#     school_id = fields.Many2one('ksba.school', string='School', required=True)
#     driver_id = fields.Many2one('res.partner', string='Driver')
#     assistant_id = fields.Many2one('res.partner', string='Assistant')
#     capacity = fields.Integer()
#     registration_number = fields.Char()
#     school = fields.Many2one('ksba.school', string='School', required=True)
#     route = fields.Many2one('ksba.route', string='Route')
#     driver = fields.Many2one('res.partner', string='Driver', domain="[('is_driver','=',True)]")
#     students = fields.Many2many('res.partner', string='Students', domain="[('is_student','=',True)]")
#     bus_locations = fields.One2many('ksba.bus.location', 'bus', string='Bus locations')