from odoo import models, fields,api

class Dock(models.Model):
    _inherit = 'stock.picking.batch'

    dock_id = fields.Many2one('custom.dock', string='Dock')
    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle')
    vehicle_category_id = fields.Many2one('fleet.vehicle.model.category', string='Vehicle Category')
    weight = fields.Float(string='Weight',compute='_compute_weight', readonly=True,store = True)
    volume = fields.Float(string = "Volume" , compute="_compute_volume",readonly=True, store = True)
    transfers = fields.Float(string="transfer" , compute= "_compute_transfers", store = True)
    lines= fields.Float(string="line",compute="_compute_lines",store = True)
    total_weight = fields.Float(readonly=True)
    total_volume = fields.Float(readonly = True)


    @api.depends("picking_ids.weight")
    def _compute_weight(self):
        for record in self:
            total_weight = 0
            for picking in record.picking_ids:
                total_weight += picking.weight
                record.total_weight = total_weight
            if record.vehicle_category_id.max_weight != 0.0:
                record.weight = (total_weight / record.vehicle_category_id.max_weight) * 100
            else:
                record.weight = 0.0

    @api.depends("picking_ids.volume")
    def _compute_volume(self):
        for record in self:
            total_volume = 0
            for picking in record.picking_ids:
                total_volume += picking.volume
                record.total_volume = total_volume
            if record.vehicle_category_id.max_volume != 0.0:
                record.volume = (total_volume / record.vehicle_category_id.max_volume) * 100
            else:
                record.volume = 0.0


    @api.depends("picking_ids")
    def _compute_transfers(self):
        for record in self:
            transfer = len(record.picking_ids)
            record.transfers = transfer

    @api.depends("move_line_ids")
    def _compute_lines(self):
        for record in self:
            line = len(record.move_line_ids)
            record.lines = line
    

    



    


   





    

    
