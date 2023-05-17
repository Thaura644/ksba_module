from odoo import fields, models


class KsbaAttendanceRecord(models.Model):
    _name = 'ksba.attendance.record'
    _description = 'Attendance record'

    bus = fields.Many2one('ksba.bus', string='Bus', required=True)
    stop = fields.Many2one('ksba.stop', string='Stop', required=True)
    date = fields.Date(default=fields.Date.today())

    students_present = fields.Many2many(
        'res.partner',
        'ksba_attendance_present_rel',
        'attendance_id',
        'student_id',
        string='Present Students',
        domain="[('is_student','=',True)]"
    )

    students_absent = fields.Many2many(
        'res.partner',
        'ksba_attendance_absent_rel',
        'attendance_id',
        'student_id',
        string='Absent Students',
        domain="[('is_student','=',True)]"
    )

    school_id = fields.Many2one('ksba.school', string='School')
