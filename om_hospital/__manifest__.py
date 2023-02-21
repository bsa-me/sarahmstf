# -*-coding: utf-8-*-

{
    'name': 'Hospital Management',
    'Version': '1.0.0',
    'summary': 'Hospital Management software',
    'sequence': 100,
    'description': """Hospital Management software""",
    'category': 'productivity',
    'website': "https://www.odoomates.tech",
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/sara.xml',
        'report/school_profile.xml',
        'report/report.xml',
    ],
    'demo': [],
    'qweb': [],
    'images':[
        'static/description/icon.png',
        'static/img/my_image.png',
    ],
    'installation': True,
    'application': True,
    'auto_install': False,
    'licence': 'LGPL-3',
}
