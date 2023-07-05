import json

from odoo import http
from odoo.http import request, Response
import googlemaps


class Main(http.Controller):
    @http.route('/get_data', type='http', methods=['GET'], auth='public', csrf=False)
    def get_data(self, **kwargs):
        #logic to recieve schools from the database
        schools = request.env['ksba.school'].sudo().search([])
        #convert schools to JSON format
        schools_json = schools.read(['name', 'address'])
        return Response(json.dumps(schools_json), content_type = 'application/json')

        data = {'example': 'example_value'}
        serialized_data =  json.dumps(data)
        return serialized_data
    

        
class Session(http.Controller):
    @http.route("/login",type='http',auth="none")
    def login(self,db,email,password,base_location=None):
            request.session.authenticate(db,email,password)
            request.env['ir.httP'].session_info()
            
class User(http.Controller):
    @http.route('/create_user', type='http', auth='public', csrf='False')
    def create_user(self, **kwargs):
        user = request.env.user
        # role = post.get('role')
        if user.has_group('base.group_erp_manager'):
            post = request.env['ksba.partners'].sudo().search(['role'])
            role = post.get('role')
            print(role)
            if role in ['parent', 'driver', 'administrator']:
                partner_data = {
                    'name': post.get('name'),
                    ' role': role,
                    'email': post.get('email'),
                    'phone': post.get('phone'),
                    'school':int(post.get('school')), 
                }
                user = request.env['res.partner'].create(partner_data)
                return "User created successfully!"
             
            else:
                return "Invalid role provided!"
        else:
            return "Access denied! You need administrator privileges to create a partner."
    
    @http.route('/signup', type='http', auth='public', website=True)
    def signup_process(self, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')
        role = kwargs.get('role')
        password = kwargs.get('password')
        user = request.env['res.users'].sudo().create({
        'name': name,
        'login': email,
        'email': email,
        'role': role,
        'password': password
        })
        partner = request.env['res.partner'].sudo().create({
            'name': name,
            'email': email,
            'user_id': user.id
        })

        return "Sign up successfully"


class BusController(http.Controller):
    @http.route('/bus_data', type='http', auth='user')
    def get_bus_data(self, bus_number=None, **kwargs):
        # Get the currently logged-in user
        user = request.env.user

        # Check if the user has a role that is associated with the bus
        if user.role in ['parent', 'driver', 'administrator']:
            # Retrieve the bus data based on the bus number
            bus = request.env['bus.model'].sudo().search([('name', '=', bus_number)])

            # Check if the bus is found
            if bus:
                # Return the bus data as a response
                return http.Response(bus)
            else:
                return http.Response("Bus not found.", status=404)
        
        return http.Response("Unauthorized access.", status=403)
    @http.route('/create_bus', type='http', auth='user', website=True)
    def create_bus(self, **post):
        user = request.env.user

        if user.role in ['administrator']:
            bus_data = {
                'plate_number': post.get('bus_name'),
                'school_id': int(post.get('school_id')),
                'capacity': int(post.get('capacity')),
                'route': int(post.get('route')),          
            }
            bus = request.env['bus.model'].create(bus_data)
            return "Bus created successfully!"
        else:
            return "Access denied! You need to be a driver to create a bus."
        
    @http.route('/update_bus/<int:bus_id>', type='http', auth='user', website=True, methods=['POST'])
    def update_bus_process(self, bus_id, **kwargs):
        # Retrieve the bus record
        bus = request.env['bus.model'].sudo().browse(bus_id)

        # Get the submitted form data
        name = kwargs.get('name')
        capacity = kwargs.get('capacity')
        school_id = kwargs.get('school_id')
        driver_id = kwargs.get('driver_id')
        route = kwargs.get('route')
        bus_locations = kwargs.get('bus_locations')
        current_location = kwargs.get('current_location')
        child_ids = kwargs.get('child_ids')

        # Update the bus details
        bus.write({
            'name': name,
            'seats': seats,
            'capacity': capacity,
            'school_id': school_id,
            'driver_id': driver_id,
            'bus_locations': bus_locations,
            'child_ids': child_ids,
            'route': route,
            
        })

        # Redirect to a success page or perform additional actions
        return "Bus Updated successfully"
    @http.route('/get_route/<int:bus_id>', type='http', auth='user',website=True, methods=['POST'])
    def get_route(origin, destination):
        api_key = env['YOURS_API_KEY']
        gmaps = googlemaps.Client(key=api_key)
        directions = gmaps.directions(origin, destination)


        if len(directions) > 0:
            #Extract information from the direction response
            route = directions[0] #get the first route (you can handle multiple routes if available)


                # Extract the duration and distance of the route
            duration = route['legs'][0]['duration']['text']
            distance = route['legs'][0]['distance']['text']

        # Extract the steps of the route
            steps = []
            for step in route['legs'][0]['steps']:
                step_info = {
                'distance': step['distance']['text'],
                'duration': step['duration']['text'],
                'instruction': step['html_instructions']
                }
                steps.append(step_info)

        # Return the extracted information or perform other actions
            return {
            'duration': duration,
            'distance': distance,
            'steps': steps
            }

        return None  # Handle no directions found or error cases