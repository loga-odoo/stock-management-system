from odoo import models, fields,api

class CustomFleetVehicle(models.Model):
    _inherit = 'fleet.vehicle.model.category'

    max_weight = fields.Float(string='Max Weight')
    max_volume = fields.Float(string='Max Volume')
    
    @api.depends('name', 'max_weight', 'max_volume')
    def _compute_display_name(self):
        for category in self:
            category.display_name = "%s (%s, %s)" % (category.name, category.max_weight, category.max_volume)






