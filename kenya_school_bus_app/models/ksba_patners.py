from odoo import models, fields, api


class Partner(models.Model):
    _name="ksba.partners"
    _inherit = 'res.partner'

    role = fields.Selection(
        selection=[
            ('parent', 'Parent'),
            ('driver', 'Driver'),
            ('administrator', 'Administrator')
        ],
        string='Role',
        default='parent'
    )

    parent_id = fields.Many2one(
        comodel_name='res.partner',
        string='Parent',
        ondelete='restrict',
        domain="[('role', '=', 'parent')]" 
    )

    child_id = fields.One2many(
        comodel_name='res.partner',
        inverse_name='parent_id',
        string='Children'
    )
    bus_id = fields.Many2one(
        comodel_name='bus.model',
        string='Bus',
        inverse_name='child_ids'
    )
    school_id = fields.Many2one(
        comodel_name='ksba.school',
        string='school'
    )
    attendance_id = fields.One2many('ksba.attendance','child_id',string='attendance')
    seat_number = fields.Integer(string='Seat Number')