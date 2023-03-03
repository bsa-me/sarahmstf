from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    custom_field = fields.Char(string='Custom Field')
    somme = fields.Float(string='Somme', compute='_compute_somme')
    school_profile_id = fields.Many2one('school.profile', string='School Profile')

    def _compute_somme(self):
        for order in self:
            order.somme = sum(line.product_uom_qty for line in order.order_line)

    def create(self, vals):
        res = super(SaleOrder, self).create(vals)
        school_profile = self.env['school.profile'].search([], limit=1)

        res.update({'school_profile_id': school_profile.id})
        return res


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    sale_order_id = fields.Many2one('sale.order', string='Sale Order')

    game_field = fields.Char(string='Game')


class InventoryOrder(models.Model):
    _inherit = 'product.template'

    price_count = fields.Integer(string="Price Count", compute='_compute_price_count')

    @api.depends('list_price')
    def _compute_price_count(self):
        for record in self:
            record.price_count = record.list_price*15000


