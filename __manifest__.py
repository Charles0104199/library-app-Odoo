{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'Manage books and authors in a library',
    'sequence': -100,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
    ],
    'installable': True,
    'application': True,
}

