from odoo import models, fields,api

class CustomFleetVehicle(models.Model):
    _inherit = 'fleet.vehicle.model.category'

    max_weight = fields.Float(string='Max Weight(kg)')
    max_volume = fields.Float(string='Max Volume(m^3)')
    
    @api.depends('name', 'max_weight', 'max_volume')
    def _compute_display_name(self):
        for category in self:
            category.display_name = "%s (%skg, %sm^3)" % (category.name, category.max_weight, category.max_volume)
            






