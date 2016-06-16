# -*- coding: utf-8 -*-
# © 2016 Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from jinja2 import Template
import pkg_resources
import os
import lxml.etree as ET
from M2Crypto import X509, RSA
import base64
import tempfile
import hashlib

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
        cls.sello = cls.get_sello()
        xml_obj = ET.fromstring(cls.xml)
        xml_obj.attrib['sello'] = cls.sello
        cls.sign_xml = ET.tostring(xml_obj)
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

    @classmethod
    def get_sello(cls):
        key_file = cls.base64_to_tempfile(key, '', '')
        (no, pem) = tempfile.mkstemp()
        os.close(no)
        cmd = ('openssl pkcs8 -inform DER -outform PEM'
               ' -in "%s" -passin pass:%s -out %s' % (key_file, pwd, pem))
        os.system(cmd)
        keys = RSA.load_key(pem)
        digest = hashlib.new('sha1', cls.cadena_original).digest()
        return base64.b64encode(keys.sign(digest, "sha1"))

    @classmethod
    def base64_to_tempfile(cls, b64_str=None, suffix=None, prefix=None):
        """ Convert strings in base64 to a temp file
        @param b64_str : Text in Base_64 format for add in the file
        @param suffix : Sufix of the file
        @param prefix : Name of file in TempFile
        """
        (fileno, file_name) = tempfile.mkstemp(suffix, prefix)
        f_read = open(file_name, 'wb')
        f_read.write(base64.decodestring(b64_str))
        f_read.close()
        os.close(fileno)
        return file_name
