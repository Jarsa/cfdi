# -*- coding: utf-8 -*-
# © 2016 Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from jinja2 import Template
import pkg_resources


class invoice(object):

    def create(self, data):
        jinja_file = pkg_resources.resource_filename('cfdi', 'data/cfdi.jinja')
        with open(jinja_file, 'r') as template:
            jinja_tmpl_str = template.read().encode('utf-8')
            tmpl = Template(jinja_tmpl_str)
            return tmpl.render(data=data)
