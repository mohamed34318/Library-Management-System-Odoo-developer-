from odoo import models, fields, api
from datetime import timedelta


class LibraryBook(models.Model):
    _name = 'library.member'
    _description = 'Library members'
    name = fields.Char('Name', required=True)
    address = fields.Char('address')
    phone = fields.Char('phone')
    picture = fields.Binary('profile picture', required=True)
    join_date = fields.Date('Join Date')
    email = fields.Char('Email', required=True)
    age = fields.Integer("Age")
    about_you = fields.Text("About You")


    #book_ids = fields.Many2many('library.book', string='Checked Out Books')








#class ResPartner(models.Model):
 #   _inherit = 'res.partner'
  #  published_book_ids = fields.One2many('library.book', 'publisher_id', string='Published Books')
   # authored_book_ids = fields.Many2many(
    #    'library.book',
     #   string='Authored Books',
        # relation='library_book_res_partner_rel' #optional
    #)
