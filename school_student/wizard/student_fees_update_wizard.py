from odoo import api, models, fields


class StudentFeesUpdateWizard(models.TransientModel):
    _name = "student.fees.update.wizard"

    price = fields.Float(string="Price")
    division = fields.Integer(string="Division")

    @api.one
    def approve_button(self):
        for record in self:
            for i in range(int(record.division)):
        student_fees_update = record.price / record.division
        distribution_obj = record.env['schools.model']
        schools = record.distribution_obj.create({'amount':division_price,'parent_id': record.id})