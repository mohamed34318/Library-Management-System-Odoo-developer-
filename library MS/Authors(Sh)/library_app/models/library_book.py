from odoo import fields, models



class Book(models.Model):
    """
    Describes a Book catalogue.
    """
    _name = "library.book"
    _description = "Book"

    picture = fields.Binary('profile picture', required=True)
    name = fields.Char(string="Name", required=True)
    date_of_birth =fields.Date(string="Birth Date")
    email =fields.Char("Email")
    phone = fields.Char("Phone Number")
    address = fields.Char(string="Address")
    note = fields.Text(string="description")
    active = fields.Boolean("Active?", default=True)