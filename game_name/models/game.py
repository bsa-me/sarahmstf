from odoo import fields, models, api



class Gamenew(models.Model):
    _name ="game.new"

    name = fields.Char()

class SaleOrder(models.Model):
   _inherit = 'sale.order'

   custom_field = fields.Char(string='Custom Field')