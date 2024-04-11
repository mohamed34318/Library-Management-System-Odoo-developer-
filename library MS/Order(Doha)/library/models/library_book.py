from datetime import timedelta

from odoo import fields, models



class Book(models.Model):
    _name = 'library.book'
    _description = 'Library Order'

   # user_id = fields.Many2one('res.users', string='User', required=True)
   # book_id = fields.Many2one('library.book', string='Book', required=True)
    author = fields.Char("Author")
    date = fields.Date(string='Order Date', default=fields.Date.today())
    return_date = fields.Date(string='Expected Return Date')
    book=fields.Char("Book")
    customer=fields.Char("Customer")
    total=fields.Integer("Total")
    num_books=fields.Integer("Number Of Books")