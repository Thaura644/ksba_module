from odoo import models, fields, api


class Partner(models.Model):
    _name="ksba.partners"
    _description = "Partners"
    _inherit = 'res.partner'


    channel_ids = fields.Many2many(
        comodel_name='ksba.channels',
        relation='ksba_partners_channels_rel',
        column1='partner_id',
        column2='channel_id',
        string='Channels'
    )

    role = fields.Selection(
        selection=[
            ('parent', 'Parent'),
            ('driver', 'Driver'),
            ('administrator', 'Administrator')
        ],
        string='role',
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
        string='Children'
    )