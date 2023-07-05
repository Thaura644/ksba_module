from odoo import models, fields

class KsbaDriver(models.Model):
    _name="ksba.driver"
    _description="Driver"
    name = fields.Char(required=True)
    home_location =  fields.Char(required=True)
    phone=fields.Integer(required=True)
    driver_role_ids= fields.One2many('ksba.partners','driver_ids',string="Driver role IDs")
    school_id=fields.Many2one('ksba.school',string="School")
    