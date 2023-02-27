from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    custom_field = fields.Char(string='Custom Field')
    somme = fields.Float(string='Somme', compute='_compute_somme')
    saleordercount = fields.Integer(string='Sale Order Count', compute='_compute_saleordercount')
    partnerid = fields.Many2one('res.partner', string='partner')


    def _compute_somme(self):
        for order in self:
            order.somme = sum(line.product_uom_qty for line in order.order_line)

    @api.depends('order_line')
   def _compute_saleordercount(self) :
    for record in self:
        record.saleordercount =len(record.order_line)


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    sale_order_id = fields.Many2one('sale.order',string='Sale Order')

    game_field = fields.Char(string='Game')

