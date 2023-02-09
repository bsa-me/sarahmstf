from odoo import models, fields, api


class school_student(models.Model):

    _name = "schools.student"
    _description = "schools_student.school_student"

    name = fields.Char()
    schools_id = fields.Many2one("school.profile", string="Schools Name")
    phone = fields.Char("phone")
    stage = fields.Selection([('pending','Pending'),('approved','Approved'),('sold','Sold'),('cancelled','Cancelled'),],default='pending',string='Stage')
    child_ids = fields.One2many('schools.model', 'parent_id', string='Checkbox')
    total_price = fields.Float(string='Total Price')
    division = fields.Float(string='Division')

    def approve_button(self):
        self.ensure_one()
        self.stage = 'approved'
        for record in self:
            for i in range(5):
                division_amount = record.total_price / record.division
            print("Iteration", i, ":", record.total_price, "divided by", record.division, "is", division_amount)
            record.child_ids.create({'amount': division_amount,
                                     'parent_id': record.id})


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
    is_selected = fields.Boolean(string='Selected')