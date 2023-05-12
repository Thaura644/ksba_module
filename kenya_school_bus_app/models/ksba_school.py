from odoo import models, fields

class KsbaSchool(models.Model):
    _name = 'kbsa.school'
    _description = 'School'
    _inherit = 'res.partner'

    # name = fields.Char(string='Name', required=True)
    # address = fields.Char(string='Address')
    # email = fields.Char(string='Email')
    # phone = fields.Char(string='Phone')
    # students = fields.One2many('res.partner', 'school_id', string='Students')
    # buses = fields.One2many('ksba.bus', 'school_id', string='Buses')
    # website = fields.Char()