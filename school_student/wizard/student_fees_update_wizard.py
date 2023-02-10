from odoo import api, models, fields


class StudentFeesUpdateWizard(models.TransientModel):
    _name = "student.feees.update.wizard"

    price = fields.Float(string="Price")
    division = fields.Integer(string="Division")

    def approve_button(self):
        print("Yeah successfully click on approve_button method........")
        return True