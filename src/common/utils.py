from pandas import CategoricalDtype

class HTTPStatus:
    OK = 200
    Created = 201
    Accepted = 202
    NoContent = 204
    BadRequest = 400
    Unauthorized = 401
    Forbidden = 403
    NotFound = 404
    MethodNotAllowed = 405
    InternalServerError = 500
    NotImplemented = 501
    BadGateway = 502
    ServiceUnavailable = 503

THRESHOLD = 0.5

FEATURE_TYPE = {
    'genero': 'category',
    'monto': 'float64',
    'hora': 'int64',
    'establecimiento': 'category',
    'ciudad': 'category',
    'is_prime': 'bool',
    'dcto': 'float64',
    'dispositivo_anio': 'int64',
    'dispositivo_marca': 'category',
    'dispositivo_proveedor': 'category',
    'num_transacciones': 'float64',
    'transacciones_establecimiento': 'float64',
    'num_establecimientos': 'float64',
    'transacciones_ciudad': 'float64',
    'num_ciudades': 'float64',
    'monto_maximo': 'float64',
    'transacciones_marca_dispositivo': 'float64',
    'transacciones_proveedor_dispositivo': 'float64',
    'transacciones_anio_dispositivo': 'float64',
    'dias_ultima_transaccion': 'float64',
    'dias_primera_transaccion': 'int64',
    'num_marcas_dispositivo': 'float64',
    'num_anios_dispositivo': 'float64',
    'num_proveedores_dispositivo': 'float64',
    'monto_promedio': 'float64',
    'monto_dst': 'float64',
    'prop_monto_linea_tc': 'float64',
    'num_dispositivos': 'float64'
 }


def anyMatchNone(obj, list):
    for element in list:
        if obj.get(element) is None:
            return True
    return False