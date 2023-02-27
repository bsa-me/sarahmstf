from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    custom_field = fields.Char(string='Custom Field')
    somme = fields.Float(string='somme', compute='_compute_somme')

    def _compute_somme(self):
        for order in self:
            order.somme = sum(line.product_uom_qty for line in order.order_line)




class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    sale_order_id = fields.Many2one('sale.order',string='Sale Order')

    game_field = fields.Char(string='Game')
    

