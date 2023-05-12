from odoo import models, fields
from lxml import etree


class KsbaRoute(models.Model):
    _name = 'ksba.route'
    _description = 'Route'
    _inherit = 'ksba.school'

    #fields definition
    name = fields.Char(required=True)
    school_id = fields.Many2one('ksba.school', string='School', required=True)
    school = fields.Many2one('ksba.school', string='School', required=True)
    stops = fields.Many2many('ksba.stop', string='Stops')
    buses = fields.One2many('ksba.bus', 'route', string='Buses')
    escription = fields.Text(string='Description')
    start_location = fields.Char(string='Start Location')
    end_location = fields.Char(string='End Location')
    distance = fields.Float(string='Distance')
    duration = fields.Float(string='Duration')
    active = fields.Boolean(string='Active', default=True)

    #relationship definition
    bus_ids = fields.Many2many(comodel_name='ksba.bus', string='Buses')
    stop_ids = fields.One2many(comodel_name='ksba.stop', inverse_name='route_id', string='Stops')

    # Views


    def action_view_buses(self):
        action = self.env.ref('ksba_school_bus_app.action_ksba_bus').read()[0]
        action['domain'] = [('route_ids', 'in', self.id)]
        action['context'] = {'default_route_ids': [(4, self.id)]}
        return action

    # Views
    def action_view_stops(self):
        action = self.env.ref('ksba_school_bus_app.action_ksba_stop').read()[0]
        action['domain'] = [('route_id', '=', self.id)]
        action['context'] = {'default_route_id': self.id}
        return action

    def action_view_buses(self):
        action = self.env.ref('ksba_school_bus_app.action_ksba_bus').read()[0]
        action['domain'] = [('route_ids', 'in', self.id)]
        action['context'] = {'default_route_ids': [(4, self.id)]}
        return action

    def action_toggle_active(self):
        for rec in self:
            rec.active = not rec.active

        return True

    # views definition

    # tree definition
    ksba_route_tree =  fields.One2many('ksba.route', 'name', string='Route Tree')
    ksba_route_tree_view ={
        'name': 'ksba.route.tree',
        'type': 'tree',
        'model': 'ksba.route',
        'arch': etree.tostring(etree.Element('tree', string='Route', )),
        'domain': [('name', '=', 'ksba.route.tree')],
        'search_view_id': 'ksba_route_search_view',
        'search_filters': '[]',
        'toolbar': {'print': []},
        'field_parent':'name',
        'field_children': 'ksba_route_tree',
        'list_view': 'ksba_route_list_view',
    }

    # form view
    ksba_route_form = fields.One2many('ksba.route', 'name', string='Route Form')
    ksba_route_form_view = {
        'name': 'ksba.route.form',
        'type': 'form',
        'model': 'ksba.route',
        'arch': etree.tostring(etree.Element('form', string='Route', )),
        'domain': [('name', '=', 'ksba.route.form')],
        'search': 'bla',
    }