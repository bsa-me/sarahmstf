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
    division = fields.Integer(string='Division')
    image = fields.Image(string="Image")
    chapter = fields.Text(string="Chapter")
    grade7 = fields.Text(string="Grade7")

    def approve_button(self):
        self.ensure_one()
        self.stage = 'approved'
        self.write({'stage':'approved'})
        for record in self:
            for i in range(int(record.division)):
                division_amount = record.total_price / record.division
                record.child_ids.create({'amount': division_amount,
                                     'parent_id': record.id})


    def sell_button(self):
        self.ensure_one()
        self.stage = 'sold'
        for line in self.child_ids:

            line.is_selected = True

    def cancel_button(self):
        self.ensure_one()
        self.stage = 'cancelled'
        for line in self.child_ids:

            line.unlink()

    def wiz_open(self):
        return {'type': 'ir.actions.act_window',
                'res_model': 'student.fees.update.wizard',
                'view_mode': 'form',
                'target': 'new'}


class ChildModel(models.Model):
    _name = 'schools.model'

    price = fields.Float(string='price')
    number = fields.Integer(string='Number')
    parent_id = fields.Many2one('schools.student', string='parent')
    amount = fields.Float(string='Amount')
    is_selected = fields.Boolean(string='Selected')