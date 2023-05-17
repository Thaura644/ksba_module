from odoo import models, fields


class KsbaSchool(models.Model):
    _name = 'ksba.school'
    _description = 'School'
    _inherit = 'res.partner'

    is_parent = fields.Boolean(string="Is Parent")
    is_driver = fields.Boolean(string="Is Driver")
    is_administrator = fields.Boolean(string="Is Administrator")

    parent_id = fields.Many2one('res.partner', string="Parent")
    child_ids = fields.One2many('res.partner', 'parent_id', string="Children")

    # def __init__(self, pool, cr):
    #     """ Update defaults for role fields """
    #     init_res = super(Partner, self).__init__(pool, cr)
    #     self._defaults.update({
    #         'is_parent': False,
    #         'is_driver': False,
    #         'is_administrator': False,
    #     })
    #     return init_res

    model_id = fields.Many2one('ir.model', string='Model', compute='_compute_model_id')
    name = fields.Char(string='Name', required=True)
    address = fields.Char(string='Address')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    school_id = fields.Many2one(
        'res.partner'
        'ksba.school', string='School'
    )
    students = fields.One2many('ksba.school', 'school_id', string='Students')
    buses = fields.One2many('ksba.bus', 'school_id', string='Buses')
    website = fields.Char()



    def _compute_model_id(self):
        for record in self:
            model = self.env['ir.model'].search([('model', '=', 'ksba.school')])
            record.model_id = model.id