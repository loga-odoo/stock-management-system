from odoo import models, fields,api

class Dock(models.Model):
    _name = 'custom.dock'

    name = fields.Char(string= "Name", required=True)

