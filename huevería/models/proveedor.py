from odoo import models, fields

class Proveedor(models.Model):

    _name = "hueveria.proveedor"
    _description = "Clase dedicada a la gestion de proveedores de la empresa"

    nombreProveedor = fields.Char(string="Nombre proveedor", required=True, help="Nombre del Proveedor")
    
    tlfProveedor = fields.Char(string="Telefono", required=True, help="Telefono del proveedor")
    
    correoProveedor = fields.Char(string="Correo del proveedor", required=True, help="Correo del proveedor")

    direccionProveedor = fields.Char(string="Direccion del proveedor", required=True, help="Direccion del proveedor")
    
    imagen_EmpresaProveedor = fields.Binary(string="Logotipo del proveedor",help="Imagen o logotipo de la empresa proveedora")

    tipoProveedor = fields.Selection([('pienso', 'Pienso'),('envases', 'Envases'),('material', 'Material')],
                                        string="Tipo de proveedor",
                                        required=True,
                                        help="Seleccione el tipo de proveedor")

    productos_ids = fields.Many2many(
    "hueveria.producto",
    relation="producto_proveedor_rel",
    column1="proveedor_id",
    column2="producto_id",
    string="Productos suministrados"
)