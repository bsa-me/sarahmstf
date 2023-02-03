from datetime import date
from odoo import fields, models, api



class SchoolProfile(models.Model):
    _name = "school.profile"

    name = fields.Char(string="school Name")
    email = fields.Char(string="Email")
    phone = fields.Char("phone")
    age = fields.Integer( string="age")
    open_date = fields.Datetime("Open Date")
    gender_type = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    date_of_birth = fields.Date(string='Date_of_Birth')
    is_teenager =fields.Char(string="Teenager?",compute='_compute_is_teenager')

    @api.depends('age')
    def _compute_is_teenager(self):
        for record in self :
            if record.age<20:
                 record.is_teenager ='Teenager'
            else:
                 record.is_teenager='Not a Teenager'
        elif record.age>=20 and record.age<=50:
                record.is_teenager='Adult'
        else:
               record.is_teenager='5etyar'






