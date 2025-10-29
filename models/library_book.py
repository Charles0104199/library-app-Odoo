from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book for users'

    name = fields.Char('Title', required=True)
    author = fields.Char('Author')
    isbn = fields.Char('ISBN')
    #published_year = fields.Integer('Published Year')
    active = fields.Boolean('Active', default=True)

