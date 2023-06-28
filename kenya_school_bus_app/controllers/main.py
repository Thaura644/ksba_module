from odoo import http
from odoo.http import request
import json
'''def action_launch(self):
user_id = self.env["res.users"].create(
            {"login": self.employee_id.work_email, "name": self.employee_id.name}
        )
self.employee_id.update({'user_id': user_id.id})'''
class Session(http.Controller):
    @http.route("/login",type='http',auth="none")
    def login(self,db,email,password,base_location=None):
        request.session.authenticate(db,email,password)
        session = http.request.session
        session_info = request.env['ir.http'].session_info()
        user = request.env.user 
        # Include the user details in the response
        response_data = [{
            'id':user.id,
            'name': user.name,
        }]
        response = http.Response(json.dumps(response_data), content_type='application/json')

        return response

    @http.route('/userdetails',type='http',auth='none')
    def get_user_details(self,db):
        session_id = http.request.httprequest.headers.get('X-Session-ID')
        session = http.request.session
        authenticated = session.authenticate(db,session_id)

        if authenticated:
            user = session.env.user
            response_data = {
                'id': user.id,
                'name': user.name,
                'email': user.email,
            }            
            return http.Response(response_data, content_type='application/json', status=200)
        else:
            return http.Response("Authentication Failed", content_type='text/plain', status=401)    
class UserController(http.Controller):
    @http.route('/getschools', type='http',auth='none')
    def get_schools(self):
        schools_rec= request.env['ksba.school'].search([])
        schools = []
        for rec in schools_rec:
            vals ={
                'id': rec.id,
                'name': rec.name,
            }
            schools.append(vals)
        data = {'status':200,'response':schools,'message':"success"}
        return http.Response(json.dumps(data), content_type='application/json', status=200)
        
    @http.route('/register', type='http', auth='none')
    def user_registration(self, **post):
        if post.get('name') and post.get('email') and post.get('password'):
            User = request.env['res.users']
            Partner = request.env['ksba.partners']
            Parent = request.env['ksba.parent']
            Child = request.env['ksba.child']
            Administrator = request.env['ksba.administrator']
            Driver = request.env['ksba.driver']
                # Check if user already exists with the given email
            existing_user = User.sudo().search([('email', '=', post['email'])])
            existing_student = User.sudo().search([('admission_no', '=', post['admission_no'])])
            if existing_user or existing_student:
                return "User with this email already exists."
            if post['role'] in ['administrator','driver','parent','child']:
                if post['role'] == 'administrator':
                    patner_id = Partner.sudo().create({'name': post['firstname']+" "+post['lastname'],'email': post['email'],'role': 'administrator'}).id
                    administrator_id = Administrator.sudo().create_user({
                            firstname: post['firstname'],
                            lastname: post['lastname'],
                            phone: post['phone'],
                            administrator_role_ids:parent_id,
                            school_id: int(post['school_id'])
                        })
                    user = User.sudo().create({
                            'name': post['firstname']+" "+post['lastname'],
                            'login': post['email'],
                            'email': post['email'],
                            'password': post['password'],
                            'partner_id':patner_id})
                elif post['role']=='child':
                    patner_id = Partner.sudo().create({
                        'name':  "hello",
                        'role':  'child',
                    }).id
                    child = Child.sudo().create({
                        firstname : post['firstname'],
                        lastname : post['lastname'],
                        home_location : post['home_location'],
                        child_role_id : patner_id,
                        school_id:int(post['school_id']),
                        adm_no : post['admission_no'],
                    })

                    user = User.sudo().create({
                    'name': post['firstname']+" "+post['lastname'],
                    'login': post['adm_no'],
                    'email': post['adm_no'],
                    'password': post['password'],
                    'partner_id':patner_id}) 
                    
                
                if user:
                    return "User registered successfully."
                else:
                    return "Failed to register user."
            else:
                return "Please provide all required fields."
        
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
                'school_id': int(post.get(' ')),
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