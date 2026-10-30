from odoo import models, fields

class Producto(models.Model):

    _name = "hueveria.producto"
    _description = "Clase dedicada a la gestion de productos de la empresa"

    nombreProducto = fields.Char(string="Nombre Producto", required=True, help="Nombre Producto")

    referenciaProducto = fields.Char(string="Referencia Producto", required=True, help="ID de referencia")

    precioProducto = fields.Float(string="Precio producto", required=True, help="Precio", default=2.99)

    cantidadProducto = fields.Integer(string="Número de cantidad", required=True, help="Cantidad", default=1)

    actividadProducto = fields.Boolean(string="Activo o no", required=True, help="Esta disponible el producto")

    fecha_RegistroProducto = fields.Date(string="Registrar fecha producto", 
                                         help="Indique la fecha", default=fields.Date.today)

    descripcionProducto = fields.Char(string="Descripción del producto", 
                                      required=True, help="Indique la descripción del productp")

    tipoProducto = fields.Selection([('huevos', 'Huevos'),('carne', 'Carne de pollo'),('otros', 'Otros productos')],
                                    string="Tipo de producto",
                                    required=True,
                                    default='huevos',
                                    help="Seleccione el tipo de producto")

    proveedores_ids = fields.Many2many(
    "hueveria.proveedor",
    relation="producto_proveedor_rel",
    column1="producto_id",
    column2="proveedor_id",
    string="Proveedores"
    )



   

    
