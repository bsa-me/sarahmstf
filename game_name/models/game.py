from odoo import fields, models, api


class SaleOrder(models.Model):
   _inherit = 'sale.order'

   custom_field = fields.Char(string='Custom Field')