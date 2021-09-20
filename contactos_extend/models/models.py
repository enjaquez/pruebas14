
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
    importe_medic    = fields.Float(string='Medicamentos', compute='_compute_importe_med')
    importe_insum    = fields.Float(string='Insumos', compute='_compute_importe_ins')
    importe_servi    = fields.Float(string='Servicios', default=0.0, readonly=True)
    importe          = fields.Float(string='Importe', compute='_compute_importe')
    impuestos        = fields.Float(string='I.V.A', default=0.0, readonly=True)
    total            = fields.Float(string='Total a pagar', default=0.0, readonly=True)

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

    def _compute_importe_med(self):
        importe_temp = 0
        for rec in self:
            datas=self.env['sale.order.line'].search([('order_partner_id','=',rec.id),('nombre_categoria','=','Medicamento')])        
        for record in datas:
            importe_temp=importe_temp + record.price_subtotal        
        self.importe_medic = importe_temp

    def _compute_importe_ins(self):
        importe_temp = 0
        for rec in self:
            datas=self.env['sale.order.line'].search([('order_partner_id','=',rec.id),('nombre_categoria','=','Insumo')])        
        for record in datas:
            importe_temp=importe_temp + record.price_subtotal        
        self.importe_insum = importe_temp

    def _compute_importe(self):
        importe_temp = 0
        importe_temp2 = 0
        importe_temp3 = 0
        for rec in self:
            datas=self.env['sale.order.line'].search([('order_partner_id','=',rec.id)])        
        for record in datas:
            importe_temp=importe_temp + record.price_subtotal
            importe_temp2=importe_temp2 + record.price_tax
            importe_temp3=importe_temp3 + record.price_total        
        self.importe = importe_temp
        self.impuestos = importe_temp2
        self.total = importe_temp3

class CustomSaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    nombre_categoria = fields.Char('Categoria',related='product_id.categ_id.name',readonly=True)


class SimpleReport(models.AbstractModel):
    _name='report.contactos_extend.report_simple_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('contactos_extend.report_simple_card')
        return {
            'doc_ids'   : docids,
            'doc_model' : self.env['res.partner'],
            'docs'      : self.env['res.partner'].browse(docids)
        }






        


