from odoo import models, fields, api


class school_student(models.Model):
    _name = "schools.student"
    _description = "schools_student.school_student"

    name = fields.Char()
    schools_id = fields.Many2one("school.profile", string="Schools Name")
    phone = fields.Char("phone")
    stage = fields.Selection([('pending','Pending'),('approved','Approved'),('sold','Sold'),('cancelled','Cancelled'),],default='pending',string='Stage')

    def approve_button(self):
        self.ensure_one()
        self.stage='approved'

    def sell_button(self):
        self.ensure_one()
        self.stage = 'sold'

    def cancel_button(self):
        self.ensure_one()
        self.stage = 'cancelled'

   class ChildModel(models.Model):
   _name = 'child.model'

   name = fields.Char(string='name')
   price = fields.Float(string='price')
   number = fields.Integer(string='Number')
   parent_id = fields.Many2one('parent.model',string='parent')

   class ParentModel(models.Model):
       _name ='parent.model'

       name = field.Char(string='name')
       child_ids = fields.One2many('child.model','parent_id',string='Children')