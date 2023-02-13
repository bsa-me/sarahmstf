from odoo import fields, models, api


class Gamenew(models.Model):
    _name ="game.new"

    name = fields.Char()