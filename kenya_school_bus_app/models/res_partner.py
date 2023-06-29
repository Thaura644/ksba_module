from odoo import models, fields, api


class KsbaPartner(models.Model):
    _name = 'res.partner'
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

    child_ids = fields.One2many(
        comodel_name='res.partner',
        inverse_name='parent_id',
        string='Children'
    )

    def set_partners(self):
        parent_partner_data = {
        'name': 'John Doe',
        'role': 'parent'
        }
        parent_partners = self.env['res.partner'].create(parent_partner_data)
        driver_partner_data = {
        'name': 'John Doe',
        'role': 'driver'
        }
        driver_partners = self.env['res.partner'].create(driver_partner_data)





    
