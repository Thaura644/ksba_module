from odoo import models, fields

class KsbaParents(models.Model):
    _name="ksba.parent"
    _description="Parent"
    firstname = fields.Char(required=True)
    lastname= fields.Char(required=True)
    home_location =  fields.Char(required=True)
    phone=  fields.Integer(required=True)
    parent_role_id= fields.One2many('ksba.partners','parent_ids',string="Parent")
    children_ids=fields.Many2one('ksba.child',string="Parent")
   