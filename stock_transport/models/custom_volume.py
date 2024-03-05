from odoo import models, fields,api

class Dock(models.Model):
    _inherit = 'stock.picking'

    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle')
    vehicle_category_id = fields.Many2one('fleet.vehicle.model.category', string='Vehicle Category')
    weight = fields.Float(string='Weight',compute='_compute_weight_percentage', readonly=True, strore = True)
    volume = fields.Float(string = "Volume" , compute="_compute_volume_percentage",readonly=True, store = True)
    


    @api.depends('move_ids', 'vehicle_category_id')
    def _compute_weight_percentage(self):
        for batch in self:
            total_weight = sum(move_line.product_id.weight * move_line.quantity for move_line in batch.move_ids)
            max_weight = batch.vehicle_category_id.max_weight if batch.vehicle_category_id else 1  # Avoid division by zero
            batch.weight = (total_weight / max_weight) * 100 if max_weight !=0 else 1000

    @api.depends('move_ids', 'vehicle_category_id')
    def _compute_volume_percentage(self):
        for batch in self:
            total_volume = sum(move_line.product_id.volume * move_line.quantity for move_line in batch.move_ids if move_line.product_id and move_line.product_id.volume)
            max_volume = batch.vehicle_category_id.max_volume
            batch.volume = (total_volume / max_volume) * 100 if max_volume !=0 else 1000
