from odoo import http
from odoo.http import request, Response
import googlemaps


class Main(http.Controller):
    @http.route('/api/get_data', type='http', methods=['GET'], auth='public', csrf=False)
    def get_data(self, **kwargs):
        # Logic to receive schools from the database
        schools = request.env['ksba.school'].sudo().search([])

        # Convert schools to JSON format
        schools_json = schools.read(['name', 'address'])

        # Generate the HTML response manually
        html_content = '''
            <html>
            <head>
                <style>
                    .school-data {
                        font-family: Arial, sans-serif;
                        background-color: #f2f2f2;
                        padding: 20px;
                    }
                    h1 {
                        margin-bottom: 10px;
                    }
                    ul {
                        list-style-type: none;
                        padding: 0;
                        margin: 0;
                    }
                    li {
                        margin-bottom: 20px;
                    }
                    strong {
                        font-weight: bold;
                    }
                </style>
            </head>
            <body>
                <div class="school-data">
                    <h1>Schools</h1>
                    <ul>
                        '''
        for school in schools_json:
            html_content += '''
                        <li>
                            <strong>Name:</strong> {}<br/>
                            <strong>Address:</strong> {}
                        </li>
                        '''.format(school['name'], school['address'])
        
        html_content += '''
                    </ul>
                </div>
            </body>
            </html>
        '''

        # Return the HTML response
        return Response(html_content, content_type='text/html')
    

        
class Session(http.Controller):
    @http.route("/api/login",type='http',auth="none", csrf='False')
    def login(self, **kwargs):
        if request.httprequest.method == 'GET':
            # csrf_token = request.csrf_token()
            return '''
            <html>
            <head>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #f2f2f2;
                        padding: 20px;
                    }
                    form {
                        background-color: #ffffff;
                        padding: 20px;
                        border-radius: 5px;
                        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                        max-width: 400px;
                        margin: 0 auto;
                    }
                    label {
                        display: block;
                        margin-bottom: 5px;
                    }
                    input[type="text"],
                    input[type="password"] {
                        width: 100%;
                        padding: 8px;
                        border-radius: 4px;
                        border: 1px solid #ccc;
                    }
                    input[type="submit"] {
                        background-color: #4CAF50;
                        color: #ffffff;
                        padding: 10px 15px;
                        border: none;
                        border-radius: 4px;
                        cursor: pointer;
                    }
                    input[type="submit"]:hover {
                        background-color: #45a049;
                    }
                </style>
            </head>
            <body>
                <form method="post">
                    <label for="db">Database:</label>
                    <input type="text" id="db" name="db">

                    <label for="email">Email:</label>
                    <input type="text" id="email" name="email">

                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password">

                    <input type="submit" value="Submit">
                </form>
            </body>
            </html>'''
        
        elif request.httprequest.method == 'POST':
            db = kwargs.get('db')
            email = kwargs.get('email')
            password = kwargs.get('password')

            if db and email and password:
                request.session.authenticate(db, email, password)
                return request.env['ir.http'].session_info()
            else:
                # Handle invalid or missing credentials
                return http.Response("Invalid credentials", status=401)
            
class User(http.Controller):
    @http.route('/api/create_user', type='http', auth='public', csrf='False')
    def create_user(self, **kwargs):
        user = request.env.user

        if request.httprequest.method == 'GET':
            # csrf_token = request.csrf_token()
            return """
            <html>
            <head>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #f2f2f2;
                    }
                    
                    .container {
                        max-width: 400px;
                        margin: 0 auto;
                        padding: 20px;
                        background-color: #fff;
                        border-radius: 5px;
                        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                    }
                    
                    .form-group {
                        margin-bottom: 20px;
                    }
                    
                    label {
                        display: block;
                        font-weight: bold;
                        margin-bottom: 5px;
                    }
                    
                    input[type="text"],
                    input[type="password"] {
                        width: 100%;
                        padding: 10px;
                        border: 1px solid #ccc;
                        border-radius: 4px;
                        box-sizing: border-box;
                    }
                    
                    input[type="submit"] {
                        background-color: #4CAF50;
                        color: #fff;
                        padding: 10px 20px;
                        border: none;
                        border-radius: 4px;
                        cursor: pointer;
                    }
                    
                    input[type="submit"]:hover {
                        background-color: #45a049;
                    }
                </style>
            </head>
            <body>
                <form method="post">
                    <label for="name">Name:</label><br>
                    <input type="text" id="name" name="name"><br><br>
                    <label for="role">Role:</label><br>
                    <input type="text" id="role" name="role"><br><br>
                    <label for="email">Email:</label><br>
                    <input type="text" id="email" name="email"><br><br>
                    <label for="phone">Phone:</label><br>
                    <input type="text" id="phone" name="phone"><br><br>
                    <label for="school">School:</label><br>
                    <input type="text" id="school" name="school"><br><br>
                    <input type="submit" value="Submit">
                </form>
            </body>
            </html>
            """

        elif request.httprequest.method == 'POST':
            # csrf_token = kwargs.get('csrf_token')
            # if not request.csrf_token() == csrf_token:
            #     return "Invalid CSRF token"

            if user.has_group('base.group_erp_manager'):
                role = kwargs.get('role')
                if role in ['parent', 'driver', 'administrator']:
                    partner_data = {
                        'name': kwargs.get('name'),
                        'role': role,
                        'email': kwargs.get('email'),
                        'phone': kwargs.get('phone'),
                        'school': int(kwargs.get('school')), 
                    }
                    user = request.env['res.partner'].create(partner_data)
                    return "User created successfully!"
                else:
                    return "Invalid role provided!"
            else:
                return "Access denied! You need administrator privileges to create a partner."
            
    @http.route('/api/signup', type='http', auth='public', website=True)
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
    @http.route('/api/bus_data', type='http', auth='user')
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

    @http.route('/api/create_bus', type='http', auth='user', website=True)
    def create_bus(self, **post):
        user = request.env.user

        if user.role in [ 'driver' ,'Administrator']:
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

    @http.route('/api/update_bus/<int:bus_id>', type='http', auth='user', website=True, methods=['POST'])
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

    @http.route('/api/get_route/<int:bus_id>', type='http', auth='user', website=True, methods=['POST'])
    def get_route(self, bus_id, **kwargs):
        origin = kwargs.get('origin')
        destination = kwargs.get('destination')

        api_key = request.env['ir.config_parameter'].sudo().get_param('google_maps.api_key')
        gmaps = googlemaps.Client(key=api_key)
        directions = gmaps.directions(origin, destination)

        if directions:
            # Extract information from the direction response
            route = directions[0]  # get the first route (you can handle multiple routes if available)

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

