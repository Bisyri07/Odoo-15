from odoo import models, fields, api

class PurchaseOrder(models.Model):  # inheritance
    _name = "master_transaksi.purchase.order"  # model name
    _description = "Purchase Order"


    item_code = fields.Char(string="Item Code")
    item = fields.Char(string="Item")
    qty = fields.Integer(string="Quantity")
    po_no = fields.Char(string='PO Number', required=True)
    po_date = fields.Datetime(string='PO Date', required=True, default=fields.Datetime.now)
    supplier_code = fields.Char(string='Supplier Code')
    supplier = fields.Char(string='Supplier')
    contact_person = fields.Char(string='Contact Person')
    term_of_payment = fields.Char(string='Term of Payment')
    expired_date = fields.Date(string='Expired Date')
    currency = fields.Many2one('res.currency', string='Currency')  # Currency field
    currency_rate = fields.Float(string='Currency Rate')
    description = fields.Text(string='Description')
    company_name = fields.Char(string='Company Name')
    discount_pct = fields.Float(string='Discount (%)')
    discount = fields.Monetary(string='Discount', currency_field='currency')  # Correct reference to currency
    ppn_pct = fields.Float(string='PPN (%)')
    ppn = fields.Monetary(string='PPN', currency_field='currency')
    pph_pct = fields.Float(string='PPH (%)')
    pph = fields.Monetary(string='PPH', currency_field='currency')
    price = fields.Monetary(string='Price', currency_field='currency')
    input_by = fields.Char(string='Input By')
    date_input = fields.Datetime(string='Date Input', default=fields.Datetime.now)
    posted_by = fields.Char(string='Posted By')
    date_posted = fields.Datetime(string='Date Posted')
    status = fields.Selection(
        [('draft', 'Draft'), ('posted', 'Posted'), ('cancelled', 'Cancelled')], 
        string='Status', default='draft'
    )

    # SQL Constraints
    _sql_constraints = [
        ('check_qty_positive', 'CHECK(qty >= 0)', 'The quantity must be positive!'),
        ('check_price_positive', 'CHECK(price > 0)', 'The price must be greater than zero!')
    ]
    
    # Field untuk menyimpan subtotal dan total
    subtotal = fields.Monetary(string='Subtotal', 
                               currency_field='currency', 
                               compute='_compute_subtotal_biaya', store=True)
    total = fields.Monetary(string='Total', 
                            currency_field='currency', 
                            compute='_compute_total_biaya', store=True)

    # computed field subtotal (price * ppn_pct / 100)
    @api.depends('price', 'ppn_pct')
    def _compute_subtotal_biaya(self):
        for a in self:
            if a.ppn_pct:
                a.subtotal = a.price * (a.ppn_pct / 100)
            else:
                a.subtotal = 0.0

    # computed field total (price + subtotal)
    @api.depends('price', 'subtotal')
    def _compute_total_biaya(self):
        for a in self:
            a.total = a.price + a.subtotal

    