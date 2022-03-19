# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
import odoo.addons.decimal_precision as dp
from odoo.exceptions import ValidationError, Warning
import logging
_logger = logging.getLogger(__name__)

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    default_alphabot_fiscal_data = fields.Boolean(string="Campos impresora fiscal", default_model='account.move')

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        params = self.env['ir.config_parameter'].sudo()
        params.set_param("default_alphabot_fiscal_data", self.default_alphabot_fiscal_data)

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        params = self.env['ir.config_parameter'].sudo()
        _value = params.get_param("default_alphabot_fiscal_data", False)
        res.update(
            default_alphabot_fiscal_data=bool(_value)
        )
        return res

class AccountMove(models.Model):
    _inherit = "account.move"
    alphabot_fiscal_data = fields.Boolean(help="Campos para imp. fiscal ...")
    alphabot_estado = fields.Char(string="Estado imp. fiscal", size=1024, copy=False)
    alphabot_cliente_name = fields.Char(string="Cliente imp. fiscal", size=1024)
    alphabot_cliente_ruc = fields.Char(string="RUC imp. fiscal", size=1024)
    alphabot_devol_fact = fields.Char(string="Factura en Devol.", size=1024)
    
    # @api.model_create_multi
    # def create(self, vals_list):
        # if not self.env.company.ValidateLicencia("FAC"):
            # raise ValidationError("Licencia de Alphabot inválida (%s)" % self.env.company.alphabot_lic_estado)                        
        # rslt = super(AccountMove, self).create(vals_list)
        # return rslt    


    def _order_fields(self,vals):
        res = super(AccountMove, self)._order_fields(vals)
        res.update({
            'alphabot_estado': vals.get('alphabot_estado') or False,
            'alphabot_cliente_name': vals.get('alphabot_cliente_name') or False,
            'alphabot_cliente_ruc': vals.get('alphabot_cliente_ruc') or False,
            'alphabot_devol_fact': vals.get('alphabot_devol_fact') or False
        })
        return res
                
    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        default = dict(default or {})
        default['alphabot_estado'] = False
        default['narration'] = False
        return super(AccountMove, self).copy(default)  

    def _reverse_moves(self, default_values_list=None, cancel=False):      
        if not default_values_list:
            default_values_list = [{} for move in self]       
        for move, default_values in zip(self, default_values_list):  
            # Esto recupera el valor de la factura tipo TFBX110050782-00000693   
            sAux = False
            if type(move.alphabot_estado) == (str): 
                if len(move.alphabot_estado) > 23:
                    sAux = move.alphabot_estado[-23:][0:22]           
            default_values.update({  
                'alphabot_devol_fact': sAux, 
                'alphabot_estado': False,     
                'narration': "",
            })    
        return super(AccountMove, self)._reverse_moves(default_values_list, cancel)          
      
                
