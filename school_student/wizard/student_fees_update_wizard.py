from odoo import api, models, fields


class StudentFeesUpdateWizard(models.TransientModel):
    _name = "student.fees.update.wizard"

    price = fields.Float(string="Price")
    division = fields.Integer(string="Division")


    def approve_button(self):
        for record in self :
            for i in range(int(record.division)):
                division_price = record.price / record.division
                distribution_obj = self.env['schools.model'].search([('id', '=', self._context.get('active_id'))])
                distribution_obj.create({'amount': division_price, 'parent_id': distribution_obj.id})