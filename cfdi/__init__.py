# -*- coding: utf-8 -*-
# © 2016 Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from jinja2 import Template
import pkg_resources
import lxml.etree as ET
from M2Crypto import X509
import base64

cer = ''  # CSD .cer in base64
key = ''  # CSD .key in base64
pwd = ''  # CSD password


class invoice(object):

    @classmethod
    def create(cls, data):
        cls.validate_data(data)
        jinja_file = pkg_resources.resource_filename('cfdi', 'data/cfdi.jinja')
        with open(jinja_file, 'r') as template:
            jinja_tmpl_str = template.read().encode('utf-8')
        tmpl = Template(jinja_tmpl_str)
        cls.xml = tmpl.render(data=data).encode('utf-8')
        cls.cadena_original = cls.generate_cadena_original(cls.xml)
        return cls

    @classmethod
    def validate_data(cls, data):
        '''
        This method will be used to validate correct input.
        @param data: python dictionary with invoide data.
        '''
        if cer and key and pwd != '':
            data['Atributos']['certificado'] = cer
            data['Atributos']['noCertificado'] = cls.get_noCertificado()
        else:
            raise ValueError(
                'You have not defined cer, key or pwd')

    @classmethod
    def generate_cadena_original(cls, xml):
        xlst_file = pkg_resources.resource_filename(
            'cfdi', 'data/cadenaoriginal_3_2.xslt')
        dom = ET.fromstring(xml)
        xslt = ET.parse(xlst_file)
        transform = ET.XSLT(xslt)
        return str(transform(dom))

    @classmethod
    def get_noCertificado(cls):
        cert = X509.load_cert_string(
            base64.decodestring(cer), X509.FORMAT_DER)
        return str(u'{0:0>40x}'.format(cert.get_serial_number()))
