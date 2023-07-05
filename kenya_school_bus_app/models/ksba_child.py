from odoo import models, fields

class KsbaChild(models.Model):
    _name = "ksba.child"
    _description ="Child"
    
    firstname = fields.Char(string="firstnanme",required=True)
    lastname= fields.Char(string="lastname",required=True)
    home_location = fields.Char(required=True,string="home_location")
    child_role_id= fields.One2many('ksba.partners','child_ids',string="Child Role ID")
    parent_ids=fields.One2many('ksba.parent','children_ids',string="Parent")
    school_id=fields.Many2one('ksba.school',string="School")
    bus_id = fields.Many2one('ksba.bus',string="Assigned Bus")
    attendance = fields.One2many('ksba.attendance','child_id',string="Attendance")
    