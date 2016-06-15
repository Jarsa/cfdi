# -*- coding: utf-8 -*-
# © 2016 Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from jinja2 import Template
import pkg_resources
import lxml.etree as ET


class invoice(object):

    def create(self, data):
        jinja_file = pkg_resources.resource_filename('cfdi', 'data/cfdi.jinja')
        with open(jinja_file, 'r') as template:
            jinja_tmpl_str = template.read().encode('utf-8')
            tmpl = Template(jinja_tmpl_str)
            xml = tmpl.render(data=data).encode('utf-8')
            cadena_original = self.generate_cadena_original(xml)
            data['cadena_original'] = cadena_original
            return xml

    def generate_cadena_original(self, xml):
        xlst = pkg_resources.resource_filename(
            'cfdi', 'data/cadenaoriginal_3_2.xslt')
        dom = ET.fromstring(xml)
        xslt = ET.parse(xlst)
        transform = ET.XSLT(xslt)
        return str(transform(dom))
