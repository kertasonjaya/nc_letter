#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class surat_masuk(models.Model):

    _name = "nc.surat_masuk"
    _description = "nc.surat_masuk"
    name = fields.Char( required=True, string="Name",  help="")
    no_surat = fields.Char( string="No surat",  help="")
    jenis_surat = fields.Char( string="Jenis surat",  help="")
    no_agenda_surat = fields.Char( string="No agenda surat",  help="")
    alur_disposisi = fields.Char( string="Alur disposisi",  help="")
    satuan_kerja = fields.Selection(selection=[('tk',"TK"),('sd',"SD"),('smp',"SMP"),('sma',"SMA")],  string="Satuan kerja",  help="")
    diterima_tanggal = fields.Date( string="Diterima tanggal",  help="")
    tanggal = fields.Date( string="Tanggal",  help="")
    asal_surat = fields.Char( string="Asal surat",  help="")
    lokasi_folder_penyimpanan = fields.Selection(selection=[('tk',"TK"),('sd',"SD"),('smp',"SMP"),('sma',"SMA"),('adm',"ADM"),('asm',"ASM"),('eksternal',"Eksternal")],  string="Lokasi folder penyimpanan",  help="")
    status = fields.Selection(selection=[('asli',"Asli"),('tembusan',"Tembusan")],  string="Status",  help="")
    sifat_surat = fields.Selection(selection=[('segera',"Segera"),('penting',"Penting"),('rahasia',"Rahasia"),('biasa',"Biasa")],  string="Sifat surat",  help="")
    prihal = fields.Char( string="Prihal",  help="")
    berkas_atau_lampiran = fields.Binary( string="Berkas atau lampiran",  help="")


    surat_keluar_ids = fields.One2many(comodel_name="nc.surat_keluar",  inverse_name="surat_masuk_id",  string="Surat keluars",  help="")
