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
    is_virtual_class= fields.Boolean(string="Virtual Class Support?",readonly="True")

    school_rank=fields.Integer(string="Rank",help="test sara's skills")
    result=fields.Float(string="Result")
    address=fields.Text(string="Address")
    documents= fields.Binary(string="Documents")
    document_name=fields.Char(string="File Name")
    currency_id=fields.Many2one("res.currency",string="currency")
    student_fees= fields.Monetary(string="Student Fees")
    total_fees=fields.Float(string="Total Fees")

     def your_button_action(self):

         self.write({'your_button_action"':'done with this'})

    @api.depends('age')
    def _compute_is_teenager(self):
        for record in self :
            if record.age<20:
                 record.is_teenager ='Teenager'

            elif record.age>=20 and record.age<=50 :
                record.is_teenager='Adult'
            else:
               record.is_teenager='5etyar'

    def your_button_action(self):
        print("hi")





