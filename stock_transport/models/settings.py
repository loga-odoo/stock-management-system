from odoo import models,fields,api
class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_stock_transport = fields.Boolean(string='Install Stock Transport Module')


    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res['module_stock_transport'] = self.env['ir.module.module'].search([('name', '=', 'stock_transport')], limit=1).state == 'installed'
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        module = self.env['ir.module.module'].search([('name', '=', 'stock_transport')], limit=1)
        if self.module_stock_transport:
            if not module:
                self.env['ir.module.module'].sudo().search([('name', '=', 'stock_transport')], limit=1).button_immediate_install()
        else:
            if module:
                module.button_uninstall()

