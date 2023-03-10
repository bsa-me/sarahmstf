from datetime import date
from odoo import fields, models, api


class SchoolProfile(models.Model):
    _name = "school.profile"
    name = fields.Char(string="school Name")
    email = fields.Char(string="Email")
    phone = fields.Char("phone")
    age = fields.Integer(string="age")
    open_date = fields.Datetime("Open Date")
    gender_type = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    date_of_birth = fields.Date(string='Date_of_Birth')
    is_teenager = fields.Char(string="Teenager?", compute='_compute_is_teenager')
    is_virtual_class = fields.Boolean(string="Virtual Class Support?", readonly="True")
    sale_order_count = fields.Integer(string="Sale Order Count")
    customer_id = fields.Many2one('res.partner', strinng='Customer')

    school_rank = fields.Selection([('public', 'Public School'), ('private', 'Private School')],
                                   string="Type of school")
    result = fields.Float(compute='_compute_result', string="result")
    address = fields.Text(string="Address")
    documents = fields.Binary(string="Documents")
    document_name = fields.Char(string="File Name")
    currency_id = fields.Many2one("res.currency", string="currency")
    student_fees = fields.Monetary(string="Student Fees")
    total_fees = fields.Float(string="Total Fees")

    # def your_button_action(self):
    #     self.write({'your_button_action"':'done with this'})

    @api.depends('age')
    def _compute_is_teenager(self):
        for record in self:
            if record.age < 20:
                record.is_teenager = 'Teenager'

            elif record.age >= 20 and record.age <= 50:
                record.is_teenager = 'Adult'
            else:
                record.is_teenager = '5etyar'

    def your_button_action(self):
        print("hi")

    @api.depends('school_rank')
    def _compute_result(self):
        for record in self:
            if record.school_rank == "private":
                record.result = 50
            elif record.school_rank == "public":
                record.result = 100
            else:
                record.result = 0

    def create_sale_orders(self):
        SaleOrder = self.env['sale.order']
        for record in self:
            customer_id = record.customer_id.id
            sale_order_count = record.sale_order_count
            for i in range(sale_order_count):
                SaleOrder.create({'partner_id': customer_id})
        return True
