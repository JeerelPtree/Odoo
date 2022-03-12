# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ptree_test(models.Model):
#     _name = 'ptree_test.ptree_test'
#     _description = 'ptree_test.ptree_test'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

#from email.policy import default
#import string
#from typing_extensions import Required
from dataclasses import field
from email.policy import default
import string
from odoo import models, fields, api


class aparcamiento(models.Model):
    _name = 'garaje.aparcamiento'
    _description = 'Permite definir las caracteristicas de un aparcamiento'

    name = fields.Char('Direccion', required=True)
    plazas = fields.Integer(string='Plazas', required=True)

    # relaciones entre tablas
    coche_ids = fields.One2many(
        'garaje.coche', 'aparcamiento_id', string='Coches')


class coche(models.Model):
    _name = 'garaje.coche'
    _description = 'Permitee definir las caracteristicas de un coche'
    _order = 'name'

    name = fields.Char(string='Matricula', required=True, size=7)
    modelo = fields.Char(string='Modelo', required=True)
    construido = fields.Date(string='Fecha de construcción')
    consumo = fields.Float('Consumo', (4, 1), default=0.0,
                           help='Consumo promedio cada 100 km')
    averiado = fields.Boolean(string='Averiado', default=False)
    # store = True no es conveniente en este caso
    annos = fields.Integer('Años', compute='_get_annos')
    descripcion = fields.Text('Descripción')

    # relacion entre tablas
    aparcamiento_id = fields.Many2one(
        'garaje.aparcamiento', string='Aparcamiento')
    mantenimiento_ids = fields.Many2many(
        'garaje.mantenimiento', string='Mantenimientos')

    @api.depends('construido')
    def get_annos(self):
        # TODO: lo dejamos para mas adelante
        for coche in self:
            coche.annos = 0


class mantenimiento(models.Model):
    _name = 'garaje.mantenimiento'
    _description = 'Permite definir mantenimiento rutinarios sobre conjutos de coches'
    _order = 'fecha'

    # name = fiels.Char()
    fecha = fields.Date('Fecha', required=True, default=fields.date.today())
    tipo = fields.Selection(string='Tipo', selection=[(
        'l', 'Lavar'), ('r', 'Revisión'), ('m', 'Mecánica'), ('p', 'Pintura')], default='l')
    coste = fields.Float('Coste', (8, 2), help='Coste total del mantenimiento')

    # relaciones entre tablas
    coche_ids = fields.Many2many('garaje.coche', string='Coches')
