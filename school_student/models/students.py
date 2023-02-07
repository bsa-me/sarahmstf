from odoo import models, fields, api

class school_student(models.Model):
    _name="schools.student"
    _description= "schools_student.school_student"

    name=fields.Char()
    schools_id=fields.Many2one("school.profile", string="Schools Name")