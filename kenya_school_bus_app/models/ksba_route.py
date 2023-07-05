from odoo import models, fields, api
from lxml import etree
import math

class KsbaRoute(models.Model):
    _name = 'ksba.route'
    _description = 'Route'

    name = fields.Char(required=True)
    stop_ids = fields.Many2many('ksba.stop', string='Stops')
    cost = fields.Float('Cost')
    buses = fields.Many2many('ksba.bus', 'route', string='Buses')
    description = fields.Text(string='Description')
    start_location = fields.Float(string='Start Location',digits=(16,6) )
    end_location = fields.Float(string='End Location',digits=(16,6))
    start_time = fields.Float('Start Time', required=True)
    end_time = fields.Float('End Time', required=True)
    student_ids = fields.Many2many('ksba.school', string='Student(s)')

    distance = fields.Float(string='Distance', compute='_compute_distance', store=True)
    duration = fields.Float(string='Duration', compute='_compute_duration', store=True)

    bus_ids = fields.Many2many('ksba.bus', string='Buses')

    