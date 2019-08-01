# -*- encoding: utf-8 -*-
{
    'name': 'Website Qweb',
    'category': 'Website',
    'sequence': 7,
    'summary': 'Some example of Qweb (website point of view)',
    'version': '1.0',
    'description': "",
    'depends': [
        'website',
    ],
    'installable': True,
    'data': [


    #assets
    'views/assets.xml',

    #layout
    'views/layout.xml',

    #pages
    'views/page/example_page.xml',

    ],
    'application': True,
}
