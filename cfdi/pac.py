# -*- coding: utf-8 -*-
# © 2016 Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import requests

pac = ''
usr = ''
pwd = ''
mode = 'test'


class drivers(object):

    @classmethod
    def stamp_pac(cls, xml):
        """
        Run methods to stamp xml.
        Get all methods with base name
        'stamp_NAME_OF_PAC'
        Invoke the methods found.
        :param string xml: cfdi ready to stamp
        :return: True
        """
        method_name_base = 'stamp_' + pac
        method_name = sorted(
            attr for attr in dir(cls) if attr.startswith(
                method_name_base)
        )
        if not method_name:
            raise ValueError(
                'You have not defined method called "%s"' % (
                    method_name_base))
        method = getattr(cls, method_name[0])
        return method(xml)

    @classmethod
    def stamp_comercio_digital(cls, xml):
        if mode == 'test':
            url = 'https://pruebas.comercio-digital.mx/timbre/TimbrarV4.aspx'
        elif mode == 'production':
            url = 'https://ws.comercio-digital.mx/timbre/TimbrarV4.aspx'
        headers = {'Content-Type': 'text/xml', 'usr': usr, 'pwd': pwd}
        stamp_xml = requests.request('POST', url, data=xml, headers=headers)
        return stamp_xml.content
