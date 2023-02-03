from datetime import datetime, timedelta
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
    age_status =fields.Char("Age Status",compute='_compute_age_status')
    @api.depends('age')
    def _compute_is_teenager(self):
        for record in self :
            if record.age<20:
                 record.is_teenager ='Teenager'
            else:
                 record.is_teenager='Not a Teenager'
    def _compute_age_status(self):
        for record in self:
            age= (datetime.now()- record.date_of_birth).days// 365
            if 20 <= age <= 50:
                record.age_status = "Adult"
            else:
                record.age_status="Not Adult"






