{
    'name': 'Kenya School Bus App',
    'version': '1.0',
    'sequence': -2221,
    'summary': 'School bus management system',
    'description': 'An efficient school bus management system with real-time tracking of buses, route optimization, and attendance management.',
    'author': 'James Mweni',
    'category': 'Extra Tools',
    'depends': ['web'],
    'data': [
   
        'security/ir.model.access.csv',
        'views/data.xml',
        'views/menu.xml',
        'views/ksba_school_views.xml',
        'views/create_user_form.xml',
        'views/ksba_bus_views.xml',
        'views/ksba_route_views.xml',
        'views/ksba_stop_views.xml',
        # 'views/ksba_attendance_record_views.xml',
        # 'views/ksba_bus_location_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
# id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
# access_ksba_school,Access KSBA School,model_ksba_school,group_parent,1,0,0,0
# access_ksba_bus,Access KSBA Bus,model_ksba_bus,group_administrator,1,1,1,1
# access_ksba_route,Access KBSA Bus,model_ksba_route,base.group_user,1,0,0,0
# access_ksba_stop,Access KSBA Stop,model_ksba_stop,base.group_user,1,0,0,0
# access_ksba_attendance_record,Access KSBA Attendance Record, model_ksba_attendance_record,base.group_user,1,0,0,0
# access_ksba_bus_location,Access KSBA Bus Location, model_ksba_bus_location,base.group_user,1,0,0,0
#
#
# access_partner_user,Partner User,model_res_partner,base.group_user,1,1,0,0
