from odoo import fields, models, api


class SaleOrder(models.Model):
   _inherit = 'sale.order'

   custom_field = fields.Char(string='Custom Field')

class PurshaseOrder(models.Model) :
   _inherit = 'purshase.order'

   organic = fields.Char(string='Organic')

   def link_sale_order(self, purshase_order_id, sale_order_id):
      purshase_order = self.browse(purshase_order_id)
      purshase_order.write({'sale_order_id': sale_order_id})
