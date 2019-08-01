# -*- encoding: utf-8 -*-
{
    'name': 'Website Qweb',
    'category': 'Website',
    'sequence': 7,
    'summary': 'Some example of Qweb (website point of view)',
    'version': '1.0',
    'description': "",
    'depends': [
        'website','website_crm',
    ],
    'installable': True,
    'data': [

    #website menu
    'data/menu.xml',

    #assets
    'views/assets.xml',

    #layout
    'views/layout.xml',

    #pages
    'views/page/without_odoo_context.xml',
    'views/page/with_odoo_context.xml',
    'views/page/some_qweb_logics.xml',
    'views/page/page_with_controller.xml',
    ],
    'application': True,
}
