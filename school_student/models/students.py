from odoo import models, fields, api


class school_student(models.Model):

    _name = "schools.student"
    _description = "schools_student.school_student"

    name = fields.Char()
    schools_id = fields.Many2one("school.profile", string="Schools Name")
    phone = fields.Char("phone")
    stage = fields.Selection([('pending','Pending'),('approved','Approved'),('sold','Sold'),('cancelled','Cancelled'),],default='pending',string='Stage')
    child_ids = fields.One2many('schools.model', 'parent_id', string='Children')
    total_price = fields.Float(string='Total Price')
    division = fields.Float(string='Division')
    def approve_button(self):
        self.ensure_one()
        self.stage = 'approved'
        for record in self:
            division_amount = record.total_price / record.division
            for line in record.child_ids:
                line.create({'amount': division_amount})

    def sell_button(self):
        self.ensure_one()
        self.stage = 'sold'

    def cancel_button(self):
        self.ensure_one()
        self.stage = 'cancelled'


class ChildModel(models.Model):
    _name = 'schools.model'

    price = fields.Float(string='price')
    number = fields.Integer(string='Number')
    parent_id = fields.Many2one('schools.student', string='parent')
    amount = fields.Float(string='Amount')
