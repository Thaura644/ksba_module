from odoo import models, fields

class KsbaAdminstrator(models.Model):
    _name="ksba.administrator"
    _description="Administrator"
    firstname = fields.Char(required=True)
    lastname= fields.Char(required=True)
    phone=fields.Integer(required=True)
    administrator_role_ids= fields.One2many('ksba.partners','adminstrator_ids',string="Administrator")
    school_id=fields.Many2one('ksba.school',string="School")
    