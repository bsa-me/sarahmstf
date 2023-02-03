from odoo import fields, models, api


class SchoolProfile(models.Model):
    _name = "school.profile"

    name = fields.Char(string="school Name")
    email = fields.Char(string="Email")
    phone = fields.Char("phone")
    age = fields.Integer("age")
    open_date= fields.Datetime("Open Date")
    gender_type=fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")






