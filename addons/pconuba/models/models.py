# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Alumno(models.Model):
    _name = 'pconuba.alumno'
    _description = 'Alumno en prácticas'

    name = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Email')
    telefono = fields.Char(string='Teléfono')
    fecha_inicio = fields.Date(string='Fecha de inicio')
    fecha_fin = fields.Date(string='Fecha de fin')
    centro_id = fields.Many2one('res.partner', string='Centro educativo')
    tarea_ids = fields.One2many('pconuba.tarea', 'alumno_id', string='Tareas')
    activo = fields.Boolean(string='Activo', default=True)

    @api.constrains('fecha_inicio', 'fecha_fin')
    def _check_fechas(self):
        for record in self:
            if record.fecha_inicio and record.fecha_fin:
                if record.fecha_fin < record.fecha_inicio:
                    raise ValidationError('La fecha de fin no puede ser anterior a la fecha de inicio.')


class Tarea(models.Model):
    _name = 'pconuba.tarea'
    _description = 'Tarea asignada a alumno'

    name = fields.Char(string='Descripción', required=True)
    alumno_id = fields.Many2one('pconuba.alumno', string='Alumno', required=True)
    responsable = fields.Selection([
        ('samuel', 'Samuel Romero'),
        ('carolina', 'Carolina Vega'),
        ('javier', 'Javier Fernández'),
    ], string='Responsable', required=True)
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_curso', 'En curso'),
        ('completada', 'Completada'),
    ], string='Estado', default='pendiente')
    fecha = fields.Date(string='Fecha')
    notas = fields.Text(string='Notas')

    @api.onchange('alumno_id')
    def _onchange_alumno(self):
        if self.alumno_id:
            self.notas = f'Tarea asignada al alumno {self.alumno_id.name}'