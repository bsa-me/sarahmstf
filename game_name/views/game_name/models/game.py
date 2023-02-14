from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    custom_field = fields.Char(string='Custom Field')



class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    sale_order_id = fields.Many2one('sale.order',string='Sale Order')

    game_field = fields.Char(string='Game')

    def link_sale_order(self, purchase_order_id, sale_order_id):
        purchase_order = self.browse(purchase_order_id)
        purchase_order.write({'sale_order_id': sale_order_id})
