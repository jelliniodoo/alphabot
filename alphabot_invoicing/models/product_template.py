# -*- coding: utf-8 -*-
from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'    
    
    # translate -> False. Esto evita que se traduzca el nombre si hay varios idiomas
    name = fields.Char('Name', index=True, required=True, translate= False)
  