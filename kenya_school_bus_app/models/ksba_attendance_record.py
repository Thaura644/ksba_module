# from odoo import fields, models
#
# class KsbaAttendanceRecord(models.Model):
#     _name = 'ksba.attendance.record'
#     _description = 'Attendance record'
#     _inherit = 'ksba.school'
#
#     bus = fields.Many2one('ksba.bus', string='Bus', required=True)
#     stop = fields.Many2one('ksba.stop', string='Stop', required=True)
#     date = fields.Date(default=fields.Date.today())
#     students_present = fields.Many2many('res.partner', string='Present Students', domain="[('is_student','=',True)]")
#     students_absent = fields.Many2many('res.partner', string='Absent Students', domain="[('is_student','=',True)]")
