from odoo import fields, models


class KsbaAttendanceRecord(models.Model):
    _name = 'ksba.attendance'
    _description = 'Attendance record'

    bus = fields.Many2one('ksba.bus', string='Bus', required=True)
    stop = fields.Many2one('ksba.stop', string='Stop', required=True)
    date = fields.Date(default=fields.Date.today())
    school_id = fields.Many2one('ksba.school', string='School')
    child_id = fields.Many2one('ksba.child',string="Student")
    seat_number = fields.Integer(required=True)    