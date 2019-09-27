# -*- encoding: utf-8 -*-
{
    'name': 'Theme Example',
    'category': 'Theme',
    'sequence': 7,
    'summary': 'A simple Theme example ',
    'version': '1.0',
    'description': 'A simple Theme example ',
    'depends': ['website','website_theme_install'],
    'images': [
        'static/description/website_theme_screenshot.jpg',
    ],
    'installable': True,
    'data': [

    #data
    'data/pictures.xml',
    'data/menu.xml',


    #assets
    'views/assets.xml',
    'views/options.xml',
    'views/snippets.xml',
    'views/snippet_options.xml',

    #layout
    'views/custom_modal.xml',


    #pages
    'views/page/form.xml',
    ],
    'application': True,
}
