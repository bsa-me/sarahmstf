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
        'reports/report.xml',
        'reports/school_profile.xml',
    ],
    'demo': [],
    'qweb': [],
    'installation': True,
    'application': True,
    'auto_install': False,
    'licence': 'LGPL-3',
}
