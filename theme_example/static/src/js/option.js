odoo.define('theme_example.editor', function(require) {
    'use strict';
    var Editor = require('web_editor.snippet.editor').Editor;
    var s_options = require('web_editor.snippets.options');

    s_options.registry.ccFx = s_options.Class.extend({

        selectClass: function(previewMode, value, $li) {
            this._super(previewMode, value, $li);
            console.log(value);
        }
    });
});
