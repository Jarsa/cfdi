.. image:: https://travis-ci.org/Jarsa/cfdi.svg?branch=master
    :target: https://travis-ci.org/Jarsa/cfdi
.. image:: https://coveralls.io/repos/github/Jarsa/cfdi/badge.svg?branch=master
    :target: https://coveralls.io/github/Jarsa/cfdi?branch=master
.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. image:: https://img.shields.io/pypi/v/cfdi.svg
    :target: https://pypi.python.org/pypi/cfdi
.. image:: https://img.shields.io/pypi/dm/cfdi.svg
    :target: https://pypi.python.org/pypi/cfdi

CFDI Python Library
===================

This library helps to make Mexico CFDI invoice.

Is in early stage.

Installation
------------

From PyPI

.. code-block::

    pip install cfdi

From local source

.. code-block::

    git clone https://github.com/Jarsa/cfdi.git
    cd cfdi
    pip install .

From remote source

.. code-block::

    pip install git+https://github.com/Jarsa/cfdi.git

How to use it?
--------------

You must use CSD ``certificate`` and ``key`` in base64.

.. code-block:: python

    # Example to convert file to base64
    import base64

    certificate = open('/path/to/certificate.cer', 'r')
    cer = base64.b64encode(certificate.read())


Assign CSD information and to generate XML then you call create method.

.. code-block:: python

    import cfdi

    cfdi.invoice.cer = cer  # cer in base64
    cfdi.invoice.key = key  # key in base64
    cfdi.invoice.pwd = pwd  # string with CSD password
    invoice = cfdi.invoice.create(data)  # to get data variable see below.

First you need to make a dictionary with invoice data with the following structure:

 .. code-block:: python

    data = {
        'Atributos': {
            'serie': 'A',  # Optional
            'folio': '12345',  # Optional
            'fecha': 'aaaa-mm-ddThh:mm:ss',  # ISO 8601
            'sello': '',  # Generated with this lib.
            'formaDePago': 'Pago en una sola exhibicion',  # Pago en una sola exhibición o número de parcialidad pagada contra el total de parcialidades, Parcialidad 1 de X.
            'noCertificado': '',  # Generated with this lib.
            'certificado': '',  # Generated with tis lib.
            'condicionesDePago': '',  # Optional
            'subTotal': '100.00',
            'descuento': '0.0',  # Optional
            'motivoDescuento': '',  # Optional
            'TipoCambio': '1.0',  # Optional
            'Moneda': 'MXN',  # Optional
            'total': '116.00',
            'tipoDeComprobante': 'ingreso',  # ingreso egreso traslado
            'metodoDePago': 'NA',  # See catalog in SAT.
            'LugarExpedicion': 'Torreon Coahuila, Mexico',
            'NumCtaPago': '1234',  # Optional
            'FolioFiscalOrig': '',  # Optional
            'SerieFolioFiscalOrig': '',   # Optional
            'FechaFolioFiscalOrig': 'aaaa-mm-ddThh:mm:ss',  # Optional ISO 8601
            'MontoFolioFiscalOrig': '0.00',  # Optional
        },
        'Emisor': {
            'rfc': 'JSI140527TS9',
            'nombre': 'Jarsa Sistemas, S.A. de C.V.',  # Optional
            'DomicilioFiscal': {
                'calle': 'Calle',
                'noExterior': '49',  # Optional
                'noInterior': '',  # Optional
                'colonia': 'Colonia',  # Optional
                'localidad': 'Torreon',  # Optional
                'referencia': 'Referencia',  # Optional
                'municipio': 'Torreon',
                'estado': 'Coahuila',
                'pais': 'Mexico',
                'codigoPostal': '27200',
            },
            'ExpedidoEn': {
                'calle': 'Calle',  # Optional
                'noExterior': '49',  # Optional
                'noInterior': '',  # Optional
                'colonia': 'Colonia',  # Optional
                'localidad': 'Torreon',  # Optional
                'referencia': 'Referencia',  # Optional
                'municipio': 'Torreon',  # Optional
                'estado': 'Coahuila',  # Optional
                'pais': 'Mexico',  # Optional
                'codigoPostal': '27200',  # Optional
            },
            'RegimenFiscal': 'Parsona Fisica con Actividad Empresarial',
        },
        'Receptor': {
            'rfc': 'XAXX010101000',
            'nombre': 'Cliente',  # Optional
            'Domicilio': {
                'calle': 'Calle',  # Optional
                'noExterior': '50',  # Optional
                'noInterior': '',  # Optional
                'colonia': 'Colonia',  # Optional
                'localidad': 'Torreon',  # Optional
                'referencia': 'Referencia',  # Optional
                'municipio': 'Torreon',  # Optional
                'estado': 'Coahuila',  # Optional
                'pais': 'Mexico',  # Optional
                'codigoPostal': '27200',  # Optional
            },
        },
        'Conceptos': [
            {
                'cantidad': '1.0',
                'unidad': 'pieza',
                'noIdentificacion': 'A123',  # Reference or serial no. Optional
                'descripcion': '',  # Optional
                'valorUnitario': '100.00',
                'importe': '100.00',
                'InformacionAduanera': {
                    'numero': '',
                    'fecha': '',
                    'aduana': '',  # Optional
                },
                'CuentaPredial': {
                    'numero': '',
                },
                'Parte': [
                    {
                        'cantidad': '1.0',
                        'unidad': 'pieza',  # Optional
                        'noIdentificacion': '',  # Optional
                        'descripcion': '',
                        'valorUnitario': '0.0',  # Optional
                        'importe': '0.0',  # Optional
                        'InformacionAduanera': {
                            'numero': '',
                            'fecha': '',
                            'aduana': '',  # Optional
                        }

                    },
                ],
            },
        ],
        'Impuestos': {
            'totalImpuestosRetenidos': '0.0',  # Optional
            'totalImpuestosTrasladados': '16.0',  # Optional
            'Retenciones': [
                {
                    'impuesto': '',  # IVA ISR
                    'importe': '0.00',

                },
            ],
            'Traslados': [
                {
                    'impuesto': 'IVA',  # IVA IEPS
                    'tasa': '16.00',
                    'importe': '16.00',
                },
            ],
        },

    }

Known issues / Roadmap
----------------------

* Sign the XML.
* Generate drivers framework to allow different PAC's.
* Hability to create Addendas.
* Test & document everything.
* Compatibility to CFDI v3.3.

Bug Tracker
-----------

Bugs are tracked on `GitHub Issues <https://github.com/Jarsa/cfdi/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed feedback `here <https://github.com/Jarsa/cfdi/issues/new?body=%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Credits
=======

Contributors
------------

* Alan Ramos <alan.ramos@jarsa.com.mx>

Maintainer
----------

.. image:: http://www.jarsa.com.mx/logo.png
   :alt: Jarsa Sistemas, S.A. de C.V.
   :target: http://www.jarsa.com.mx

This package is maintained by Jarsa Sistemas, S.A. de C.V.