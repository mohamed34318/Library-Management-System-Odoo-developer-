from odoo import api,fields,models
class issues_books(models.Model):
    _name = "library.issues_books"
    _description = "The issues books in a library refer to books that have been identified as having problems such as damage"

    name = fields.Char(string="name of book")
    age = fields.Integer(string="book age")
    description= fields.Text(string="library")
    total_copy_of_book = fields.Integer(string="number of issues_books")
    number_of_copy_damaged = fields.Integer(string="number of issues_books")
    available_copy_of_book = fields.Integer(string="available of number issues_books")
    number_of_copy_issues = fields.Integer(string="number of issues_books")





