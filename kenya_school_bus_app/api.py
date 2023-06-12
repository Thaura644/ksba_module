from odoo import http
from odoo.http import request 
from odoo.addons.web.controllers.main import import serialize_exception


class KenyaSchoolBusAPI(http.Controller):
    #api endpoint for retrieving schools
    @http.route('/kenya_school_bus_app/api/schools', auth='none', methods=['GET'], csrf=False, type='json')
    @serialize_exception
    def get_schools(self, **kwargs):
        schools = request.env['ksba_school'].sudo().search([]) #retrieve all schools
        return schools.read(['name', 'address', 'phone']) #return selected fields as JSON
    
    #API endpoint for retrieveing buses
    @http.route('/kenya_school_bus_app/api/buses', auth='none', methods=['GET'], csrf=False, type='json')
    @serialize_exception
    def get_buses(self, **kwargs):
        buses = request.env['ksba_bus'].sudo().search([]) #retrieve all buses
        return buses.read(['name', 'licence_plate', 'capacity']) # return selected fields as JSON
    

     #API endpoint for retrieveing routes
    @http.route('/kenya_school_bus_app/api/routes', auth='none', methods=['GET'], csrf=False, type='json')
    @serialize_exception
    def get_routes(self, **kwargs):
        routes = request.env['ksba_route'].sudo().search([]) #retrieve all routes and stops
        return routes.read(['']) # return selected fields as JSON
    

     #API endpoint for retrieveing buses
    @http.route('/api/kenya_school_bus_app/attendances', auth='none', methods=['GET'], csrf=False, type='json')
    @serialize_exception
    def get_attendances(self, **kwargs):
        attendances = request.env['ksba_attendance_record'].sudo().search([]) #retrieve the attendance record
        return attendances.read([]) # return selected fields as JSON
    


    