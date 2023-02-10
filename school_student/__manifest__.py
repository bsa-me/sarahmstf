#-*-coding: utf-8-*-
{
    'name': "school_student",
    'Version': '0.1',
    'summary': """Short (1 phrase/line) summary of the module's purpose, used as 
                  subtitle on modules listing or apps.openerp.com""",
    'sequence': 100,
    'description':""" Long description of module's purpose""",
    'category': 'uncategorized',
    'author':"My Company",
    'website': "https://www.yourcompany.com",
    'depends': ['base','school'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'wizard/student_fees_udpdate_wizard_view.xml'
    ],
    'demo': [
        'demo/demo.xml'
    ],

}

