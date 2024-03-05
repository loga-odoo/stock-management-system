from odoo import models,fields
class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_stock_transport = fields.Boolean(string='Install Stock Transport Module')

