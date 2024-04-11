{
    "name": "Library Management",
    "summary": "Manage library catalog and book lending.",
    "description" : """
    this is my library,a big library
    """,
    "author": "shaimaa farag",
    "license": "AGPL-3",
    "website": "https://github.com/PacktPublishing"
               "/Odoo-15-Development-Essentials",
    "version": "15.0.1.0.0",
    "category": "Services/Library",
    "depends": ["base"],
    "data": [
        "security/library_security.xml",
        "security/ir.model.access.csv",
        "views/library_menu.xml",
        ],
    "application": False,
}
