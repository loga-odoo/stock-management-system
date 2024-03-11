from odoo import fields, models, api


class stockpicking(models.Model):
    _inherit = "stock.picking"

    weight = fields.Float(string="Weight", compute="_cal_weight", store="True")
    volume = fields.Float(string="Volume", compute="_cal_volume", store="True")

    @api.depends("product_id", "product_id.weight", "move_line_ids.quantity")
    def _cal_weight(self):
        for record in self:
            cal_weight = 0
            for move in record.move_line_ids:
                cal_weight += move.product_id.weight * move.quantity
            record.weight = cal_weight

    @api.depends("product_id", "product_id.volume", "move_line_ids.quantity")
    def _cal_volume(self):
        for record in self:
            cal_volume = 0
            for move in record.move_line_ids:
                cal_volume += move.product_id.volume * move.quantity
            record.volume = cal_volume
