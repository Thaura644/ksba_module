import json

from odoo import http
from odoo.http import request, Response


class KsbaApiController(http.Controller):
    @http.route('/kenya_school_bus_app/api/get_data', type='http', methods=['GET'], auth='public', csrf=False)
    def get_data(self, **kwargs):
        #logic to recieve schools from the database
        schools = request.env['ksba.school'].sudo().search([])
        #convert schools to JSON format
        schools_json = schools.read(['name', 'address'])
        return Response(json.dumps(schools_json), content_type = 'application/json')

        data = {'example': 'example_value'}
        serialized_data =  json.dumps(data)
        return serialized_data
    
    # @http.route('kenya_school_bus_app/api/partners', methods=['GET'], auth='public', type='json')



    @http.route('/kenya_school_bus_app/api/create_admin', methods=['POST'], type='json', auth='public')
    def create_admin(self, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')

        # Validate and process the form data as needed

        admin_data = {
            'name': name,
            'email': email,
            'role': 'administrator'
        }

        admin_partner = http.request.env['res.partner'].sudo().create(admin_data)

        # Additional logic or response handling

        return {'result': 'success', 'admin_id': admin_partner.id}
    @http.route('/kenya_school_bus_app/api/partners', methods=['GET'], auth='public', type='json')
    def get_partners(self):
        partners = http.request.env['res.partner'].sudo().search([])
        partner_data = []
        for partner in partners:
            partner_data.append({
                'name': partner.name,
                'role': partner.role
            })
        return {'result': 'success', 'data': partner_data}

    
    @http.route('/kenya_school_bus_app/api/schools', methods=['GET'], auth='public', type='json')

    def get_schools(self, **kwargs):
        schools = request.env['ksba_school'].sudo().search([]) #retrieve all schools
        return schools.read(['name', 'address', 'phone']) #return selected fields as JSON
    
    #API endpoint for retrieveing buses
    @http.route('/kenya_school_bus_app/api/buses', methods=['GET'], auth='public', type='json')
    def get_buses(self, **kwargs):
        buses = request.env['ksba_bus'].sudo().search([]) #retrieve all buses
        return buses.read(['name', 'number_plate', 'capacity', 'route', 'model']) # return selected fields as JSON
    

     #API endpoint for retrieveing routes
    @http.route('/kenya_school_bus_app/api/routes', methods=['GET'], auth='public', type='json')
    def get_routes(self, **kwargs):
        routes = request.env['ksba_route'].sudo().search([]) #retrieve all routes and stops
        return routes.read(['name', 'description', 'school', 'distance', 'duration']) # return selected fields as JSON
    

     #API endpoint for retrieveing attendance
    @http.route('/kenya_school_bus_app/api/attendances', methods=['GET'], auth='public', type='json')
    def get_attendances(self, **kwargs):
        attendances = request.env['ksba_attendance_record'].sudo().search([]) #retrieve the attendance record
        return attendances.read(['bus', 'stop', 'date']) # return selected fields as JSON
    


