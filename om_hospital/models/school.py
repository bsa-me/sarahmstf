from odoo import fields, models, api


class SchoolProfile(models.Model):
    _name = "school.profile"

    name = fields.Char(string="school Name")
    email = fields.Char(string="Email")
    phone = fields.Char("phone")
    age = fields.Integer("age")
    open_date= fields.datetime("Open Date")
    school_type=fields.selection([('public',public School'),('private',private School')],string="Type of School",
                                 help="please select School Type.",default='private')






