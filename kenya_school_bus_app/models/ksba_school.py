
from odoo import models, fields


class KsbaSchool(models.Model):
    _name = 'ksba.school'
    _description = 'School'

    model_id = fields.Many2one('ir.model', string='Model', compute='_compute_model_id')
    name = fields.Char(string='Name', required=True)
    address = fields.Char(string='Address')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    students = fields.One2many('ksba.child', 'school_id', string='Students')
    buses_id = fields.One2many('ksba.bus', 'school_id', string='Buses')
    attendance_ids = fields.One2many('ksba.attendance', 'school_id', string='Attendance')
    website = fields.Char()
    driver_ids=fields.One2many('ksba.driver',"school_id", string="Drivers")
    administrator_ids = fields.One2many('ksba.administrator','school_id', string="Administrators")
    
