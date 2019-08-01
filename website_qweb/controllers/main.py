# -*- coding: utf-8 -*-
from odoo import http, models, fields, _
from odoo.http import request

class WebsiteQweb(http.Controller):
    @http.route(['/page_with_controller'], type='http', auth="public", website=True, multilang=True)
    def page_with_controller(self):
        #some logics & return the template
        return request.render('website_qweb.page_with_controller',{'variable':'My 🤘 Variable'})
