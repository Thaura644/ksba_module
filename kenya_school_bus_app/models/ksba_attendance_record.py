from odoo import fields, models, api
# from odoo.api import api


class KsbaAttendanceRecord(models.Model):
    _name = 'ksba.attendance'
    # _inherit = 'mail.thread'
    _description = 'Attendance record'
    _order = "attendance_date desc"


    name = fields.Char('Name', readonly=True, size=32)
    attendance_date = fields.Date(
        'Date', required=True, default=lambda self: fields.Date.today(),
        tracking=True)
    bus = fields.Many2one('ksba.bus', string='Bus', required=True)
    stop = fields.Many2one('ksba.stop', string='Stop', required=True)
    date = fields.Date(default=fields.Date.today())
    school_id = fields.Many2one('ksba.school', string='School')
    child_id = fields.Many2one('ksba.child',string="Student")
    seat_number = fields.Integer(required=True)
    state = fields.Selection(
        [('draft', 'Draft'), ('start', 'Attendance Start'),
         ('done', 'Attendance Taken'), ('cancel', 'Cancelled')],
        'Status', default='draft', tracking=True)  


    def attendance_draft(self):
        self.state = 'draft'

    def attendance_start(self):
        self.state = 'start'

    def attendance_done(self):
        self.state = 'done'

    def attendance_cancel(self):
        self.state = 'cancel'

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            sheet = self.env['ir.sequence'].next_by_code('ksba.attendance')
            vals['name'] = sheet
        return super(KsbaAttendanceRecord, self).create(vals_list)