from odoo import models, fields

class PurchaseOrder(models.Model):  # inheritance
    _name = "master_transaksi.purchase.order"  # model name
    _description = "Purchase Order"

    po_no = fields.Char(string='PO Number', required=True)
    po_date = fields.Date(string='PO Date', required=True)
    supplier_code = fields.Char(string='Supplier Code')
    supplier = fields.Char(string='Supplier')
    contact_person = fields.Char(string='Contact Person')
    term_of_payment = fields.Char(string='Term of Payment')
    expired_date = fields.Date(string='Expired Date')
    currency = fields.Many2one('res.currency', string='Currency', required=True)  # Currency field
    currency_rate = fields.Float(string='Currency Rate')
    description = fields.Text(string='Description')
    company_name = fields.Char(string='Company Name')
    discount_pct = fields.Float(string='Discount (%)')
    discount = fields.Monetary(string='Discount', currency_field='currency')  # Correct reference to currency
    ppn_pct = fields.Float(string='PPN (%)')
    ppn = fields.Monetary(string='PPN', currency_field='currency')
    pph_pct = fields.Float(string='PPH (%)')
    pph = fields.Monetary(string='PPH', currency_field='currency')
    amount = fields.Monetary(string='Amount', currency_field='currency')
    subtotal = fields.Monetary(string='Subtotal', currency_field='currency')
    total = fields.Monetary(string='Total', currency_field='currency')
    input_by = fields.Char(string='Input By')
    date_input = fields.Datetime(string='Date Input', default=fields.Datetime.now)
    posted_by = fields.Char(string='Posted By')
    date_posted = fields.Datetime(string='Date Posted')
    status = fields.Selection(
        [('draft', 'Draft'), ('posted', 'Posted'), ('cancelled', 'Cancelled')], 
        string='Status', default='draft'
    )
    # uom = fields.Char(string='UOM')
    # po_type = fields.Char(string='PO Type')