from odoo import models, fields,api

class Dock(models.Model):
    _inherit = 'stock.picking.batch'

    dock_id = fields.Many2one('stock.picking.batch', string='Dock')
    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle')
    vehicle_category_id = fields.Many2one('fleet.vehicle.model.category', string='Vehicle Category')
    weight = fields.Float(string='Weight',widget = "progress" ,compute='_compute_weight_percentage', readonly=True)


    @api.depends('move_line_ids', 'vehicle_category_id')
    def _compute_weight_percentage(self):
        for batch in self:
            total_weight = sum(move_line.product_id.weight * move_line.quantity for move_line in batch.move_line_ids)
            max_weight = batch.vehicle_category_id.max_weight if batch.vehicle_category_id else 1  # Avoid division by zero
            batch.weight = (total_weight / max_weight) * 100

   





    

    
