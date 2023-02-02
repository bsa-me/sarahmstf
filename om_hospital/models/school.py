from odoo import fields, models, api


class schoolprofile(models,Model):
    _name="school.profile"

    name=fields.Char(string="school Name")
    email=fields.Char(string="Email")
    phone=fields.Char("phone")