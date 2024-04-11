from odoo import api,fields,models
class book_requests(models.Model):
    _name = "library.book_requests"
    _description = "library.book_requests"

    name = fields.Char(string="name of book",required=True)
    user_id = fields.Integer(string="user_id",required=True)
    book_id = fields.Integer(string="Book_id")
    request_date = fields.Date(string="request_date",required=True)
    return_date = fields.Date(string="return_date",required=True)
    state = fields.Char(string="state_of_request")
    edition = fields.Integer(string="number_of_edition")
    requested_by = fields.Char(string="name_of_user",required=True)
    author = fields.Char(string="name of auther")