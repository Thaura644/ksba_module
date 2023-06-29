from odoo import models, fields, api


class Partner(models.Model):
    _name="ksba.partners"
    _inherit = 'res.partner'

    role = fields.Selection(
        selection=[
            ('parent', 'Parent'),
            ('driver', 'Driver'),
            ('administrator', 'Administrator'),
            ('student', 'Student'),
        ],
        string='Role',
        default='parent'
    )

    parent_ids = fields.Many2one(
        comodel_name='ksba.parent',
        string='Parents',
        ondelete='restrict',
        domain="[('role', '=', 'parent')]" 
    )
    driver_ids = fields.Many2one(
        comodel_name='ksba.driver',
        string='Drivers',
        ondelete='restrict',
        domain="[('role', '=', 'driver')]" 
    )
    adminstrator_ids = fields.Many2one(
        comodel_name='ksba.adminstrator',
        string='administrators',
        ondelete='restrict',
        domain="[('role', '=', 'administrator')]" 
    )

    child_ids = fields.Many2one(
        comodel_name='ksba.child',
        string='Children',
        ondelete='restrict',
        domain=[('role', '=', 'student')]
    )
