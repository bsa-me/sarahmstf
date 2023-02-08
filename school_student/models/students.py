from odoo import models, fields, api

class school_student(models.Model):
    _name="schools.student"
    _description= "schools_student.school_student"

    name=fields.Char()
    schools_id=fields.Many2one("school.profile", string="Schools Name")
    phone=fields.Char("phone")
    stage= fields.Selection([('pending','Pending'),('approved','Approved'),],default='pending',string='Stage')
    def approve_button(self):
        self.ensure_one()
        self.stage='approved'