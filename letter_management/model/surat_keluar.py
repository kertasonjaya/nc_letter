#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class surat_keluar(models.Model):

    _name = "nc.surat_keluar"
    _description = "nc.surat_keluar"
    name = fields.Char( required=True, string="Name",  help="")


    surat_masuk_id = fields.Many2one(comodel_name="nc.surat_masuk",  string="Surat masuk",  help="")
