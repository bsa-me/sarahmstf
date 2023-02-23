from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    custom_field = fields.Char(string='Custom Field')

    def _compute_order_quantity(self):
        for record in self:
            total_qty = 0
            for line in record.order_line:
                total_qty += line.product_uom_qty
            record.order_quantity = total_qty



class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    sale_order_id = fields.Many2one('sale.order',string='Sale Order')

    game_field = fields.Char(string='Game')

