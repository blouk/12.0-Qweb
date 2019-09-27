from odoo import models

class ThemeExample(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_example_post_copy(self, mod):
        self.enable_view('website.option_font_title_02_variables')
        self.enable_view('website.option_font_body_03_variables')
        self.enable_view('website.option_font_button_04_variables')
        self.enable_view('website.option_font_navbar_06_variables')
        self.disable_view('website_theme_install.customize_modal')
