# -*- coding: utf-8 -*-
{
    'name': "hueveria",
    'summary': "Huevería Avicola Ebro",
    'description': "Gestión de la Huevería de Avícola Ebro ",
    'author': "Jorge",
    'website': "",
    'category': "Tools",
    'version': '0.1',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
    'security/ir.model.access.csv',
    'views/gestor_view.xml',
    'views/gestorProv_view.xml',
],

    'installable': True,
    'application': True,
}