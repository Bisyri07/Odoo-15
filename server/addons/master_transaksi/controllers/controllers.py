# -*- coding: utf-8 -*-
# from odoo import http


# class MasterTransaksi(http.Controller):
#     @http.route('/master_transaksi/master_transaksi', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/master_transaksi/master_transaksi/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('master_transaksi.listing', {
#             'root': '/master_transaksi/master_transaksi',
#             'objects': http.request.env['master_transaksi.master_transaksi'].search([]),
#         })

#     @http.route('/master_transaksi/master_transaksi/objects/<model("master_transaksi.master_transaksi"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('master_transaksi.object', {
#             'object': obj
#         })
