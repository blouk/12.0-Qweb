# -*- encoding: utf-8 -*-
{
    'name': 'Theme Example',
    'category': 'Theme/Creative',
    'sequence': 7,
    'summary': 'A simple Theme example ',
    'version': '1.0',
    'description': "",
    'depends': ['theme_common'],
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
    'views/snippet_options.xml',

    #layout

    #pages
    'views/page/form.xml',
    ],
    'application': True,
}
