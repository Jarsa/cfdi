# -*- coding: utf-8 -*-
# © 2016 Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import unittest
import cfdi
from datetime import datetime


class MainTest(unittest.TestCase):
    def setUp(self):
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

    def test_10_generate_xml(self):
        '''Generate xml first time'''
        invoice = cfdi.invoice()
        invoice.create(self.data)
