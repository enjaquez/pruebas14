
# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
import datetime

class Generos(models.Model):
	_name = 'contactos_extend.generos'
	_description = 'Generos'

	name = fields.Char(string="Genero")

class GrupoRh(models.Model):
	_name = 'contactos_extend.gruporh'
	_description = 'Grupo Rh'

	name = fields.Char(string="Grupo Rh")

class TiposPaciente(models.Model):
	_name = 'contactos_extend.tipospaciente'
	_description = 'Tipos de Paciente'

	name = fields.Char(string="Tipo de Paciente")

class EstadoCivil(models.Model):
	_name = 'contactos_extend.estadocivil'
	_description = 'Estado Civil'

	name = fields.Char(string="Estado Civil")

class Cuartos(models.Model):
	_name = 'contactos_extend.cuartos'
	_description = 'Cuartos'

	name = fields.Char(string="Cuarto")
	detalle = fields.Html(string="Detalle")

class Especialidades(models.Model):
	_name = 'contactos_extend.especialidades'
	_description = 'Especialidades'

	name = fields.Char(string="Especialidades")

class Medicos(models.Model):
	_name = 'contactos_extend.medicos'
	_description = 'Medicos'

	name = fields.Char(string="Medico")



class CustomContactos(models.Model):

    _inherit = 'res.partner'

    count_reg        = fields.Integer(compute="_calculo_registro")
    es_paciente      = fields.Boolean(string="Es un paciente?")
    folio            = fields.Char(string='Folio')
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")
    fecha_ingreso    = fields.Datetime(string="Fecha de Ingreso")
    edad             = fields.Float(string="Edad")
    alergias         = fields.Boolean(string="Alergias")
    servicio         = fields.Char(string="Servicio")
    motivo_consulta  = fields.Html(string="Notas")
    ocupacion        = fields.Char(string='Ocupacion')
    genero           = fields.Many2one(comodel_name='contactos_extend.generos', string="Genero")
    gruporh          = fields.Many2one(comodel_name='contactos_extend.gruporh', string="Grupo Rh")
    tipospaciente    = fields.Many2one(comodel_name='contactos_extend.tipospaciente', string="Tipos de Paciente")
    estadocivil      = fields.Many2one(comodel_name='contactos_extend.estadocivil', string="Estado Civil")
    cuarto           = fields.Many2one(comodel_name='contactos_extend.cuartos', string="Cuarto")
    especialidad     = fields.Many2one(comodel_name='contactos_extend.especialidades', string="Especialidad")
    medico           = fields.Many2one(comodel_name='contactos_extend.medicos', string="Medico")
    importe_medic    = fields.Float(string='Medicamentos', default=0.0)
    importe_insum    = fields.Float(string='Insumos', default=0.0)
    importe_servi    = fields.Float(string='Servicios', default=0.0)
    importe          = fields.Float(string='Importe', default=0.0)
    impuestos        = fields.Float(string='I.V.A', default=0.0)
    total            = fields.Float(string='Total a pagar', default=0.0)

    def get_medicamentos(self):
    	self.ensure_one()
    	return {
    		'type': 'ir_actions.act_window',
    		'name': 'Medicamentos',
    		'view_mode': 'tree,form',
    		'res_model': 'contactos_extend.medicos',
    		#'domain': 
    		#'context': '{"create","False"}'
    	}

    def _calculo_registro(self):
    	for rec in self:
    		rec.count_reg=self.env['sale.order.line'].search_count([('order_partner_id','=',rec.id)])


class CustomSaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    categoria = fields.Many2one('product.template',string='Categoria')
    nombre_categoria = fields.Char('Categoria',related='categoria.categ_id',readonly=True)



