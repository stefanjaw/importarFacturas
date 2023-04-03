# -*- coding: utf-8 -*-

from odoo import models, fields, api
class Invoice(models.Model):
    _inherit = "account.move"
    clave_proveedor = fields.Char(string="Clave Proveedor", )
    numero_consecutivo_aceptacion = fields.Char(string="Numero Consecutivo Aceptación", )

class CurrencyRate(models.Model):
    _inherit = "res.currency.rate"
    rate = fields.Float(string="Rate", digits=(18, 12))

class Currency(models.Model):
    _inherit = "res.currency"
    rate = fields.Float(string="Rate", digits=(18, 12))

class Partner(models.Model):
    _inherit = 'res.partner'
    tipo_cedula = fields.Selection([
        ('01', 'Cédula Física'),
        ('02', 'Cédula Jurídica'),
        ('03','DIMEX'),
        ('04','NITE'),
    ], string='Tipo')
