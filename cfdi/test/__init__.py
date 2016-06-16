# -*- coding: utf-8 -*-
# © 2016 Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import unittest
import base64
import cfdi
import pkg_resources
from datetime import datetime


class MainTest(unittest.TestCase):
    def setUp(self):
        cer_file = pkg_resources.resource_filename(
            'cfdi', 'test/CSD01_AAA010101AAA.cer')
        cer = open(cer_file, 'r')
        self.cer = base64.b64encode(cer.read())
        key_file = pkg_resources.resource_filename(
            'cfdi', 'test/CSD01_AAA010101AAA.key')
        key = open(key_file, 'r')
        self.key = base64.b64encode(key.read())
        self.pwd = '12345678a'
        self.data = {
            'Atributos': {
                'serie': 'A',
                'folio': '12345',
                'fecha': datetime.now().isoformat(),
                'formaDePago': 'Pago en una sola exhibicion',
                'noCertificado': '00001000000202599785',
                'certificado': 'certificado',
                'subTotal': '100.00',
                'total': '116.00',
                'tipoDeComprobante': 'ingreso',
                'metodoDePago': 'NA',
                'LugarExpedicion': 'Torreon Coahuila, Mexico',
            },
            'Emisor': {
                'rfc': 'JSI140527TS9',
                'nombre': 'Jarsa Sistemas, S.A. de C.V.',
                'DomicilioFiscal': {
                    'calle': 'Gardenias',
                    'noExterior': '49',
                    'noInterior': False,
                    'colonia': 'Torreon Jardin',
                    'localidad': 'Torreon',
                    'municipio': 'Torreon',
                    'estado': 'Coahuila',
                    'pais': 'Mexico',
                    'codigoPostal': '27200',
                },
                'RegimenFiscal': 'Persona Moral del Regimen General',
            },
            'Receptor': {
                'rfc': 'XAXX010101000',
                'nombre': 'Cliente',
                'Domicilio': {
                    'calle': 'Calle',
                    'noExterior': 'Sin Numero',
                    'noInterior': False,
                    'colonia': False,
                    'localidad': 'Torreon',
                    'municipio': 'Torreon',
                    'estado': 'Coahuila',
                    'pais': 'Mexico',
                    'codigoPostal': '27200',
                },
            },
            'Conceptos': [
                {
                    'cantidad': '1.0',
                    'unidad': 'pieza',
                    'noIdentificacion': 'A123',
                    'valorUnitario': '100.00',
                    'importe': '100.00',
                },
            ],
            'Impuestos': {
                'totalImpuestosRetenidos': '0.0',
                'totalImpuestosTrasladados': '16.0',
                'Traslados': [
                    {
                        'impuesto': 'IVA',
                        'tasa': '16.00',
                        'importe': '16.00',
                    },
                ],
            },

        }

    def tearDown(self):
        cfdi.cer = ''
        cfdi.key = ''
        cfdi.pwd = ''

    def test_10_generate_xml(self):
        '''Generate xml first time'''
        cfdi.cer = self.cer
        cfdi.key = self.key
        cfdi.pwd = self.pwd
        cfdi.invoice.create(self.data)

    def test_20_no_cer_key_pwd(self):
        '''Test when cer, key and pass is not defined'''
        with self.assertRaisesRegexp(
                ValueError, 'You have not defined cer, key or pwd'):
            cfdi.invoice.create(self.data)
