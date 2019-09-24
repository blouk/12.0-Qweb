# -*- coding: utf-8 -*-
from odoo import http, models, fields, _
from odoo.http import request

class WebsiteForm(http.Controller):
    @http.route(['/form'], type='http', auth="user", website=True, methods=['POST','GET'])
    def form_website(self, **post):
        user = request.env.user.partner_id

        if request.httprequest.method == 'POST':
            user.write({
                'email': post['email'],
                'company_name': post['company'],
                'website': post['website'],
            })

        return request.render('theme_example.form_user',{ 'user': user })
