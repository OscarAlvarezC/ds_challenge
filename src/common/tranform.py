import pandas as pd
from sklearn import preprocessing
import numpy as np

def cumulative_compute(df, order_fields, pivot, value, function, name=None):
    df_sorted = df.sort_values(order_fields)
    if df_sorted[value].dtype == 'object':
        df_sorted[value] = preprocessing.LabelEncoder().fit_transform(df_sorted[value]) 
    s = df_sorted.groupby(pivot)[value].expanding().agg(function)
    s = s.droplevel(list(range(len(pivot))))
    if name != None:
        s.rename(name, inplace=True)
    return s

def rolling_compute(df, order_fields, pivot, value, function, window, name):
    df_sorted = df.sort_values(order_fields)
    s = df_sorted.groupby(pivot)[value].rolling(window).agg(function)
    s = s.droplevel(list(range(len(pivot)))).rename(name)
    return s

def vectorized_compute(df, order_fields, pivot, value, function, name=None):
    df_sorted = df.sort_values(order_fields)
    s = df_sorted.groupby(pivot)[value].agg(function)
    if name != None:
        s.rename(name, inplace=True)
    return s

def transform(data):
    data.fecha = pd.to_datetime(data.fecha, format='%d/%m/%y') + pd.to_timedelta(data.hora, unit='h')
    # Evaluating string for get json structure
    data.dispositivo = data.dispositivo.map(lambda x: eval(x) if pd.notnull(x) else x)
    # Transform data to DataFrame
    device_df = data.dispositivo.apply(pd.Series)
    device_df.rename(columns={'año':'anio'}, inplace=True)
    data = pd.concat([data, device_df.add_prefix('dispositivo_')], axis=1)

    data = data.join(cumulative_compute(data, ['fecha','transaction_id'], ['user_id'], 'transaction_id', 'count', 'num_transacciones'))
    data = data.join(cumulative_compute(data, ['fecha','transaction_id'], ['user_id','establecimiento'], 
                                    'transaction_id', 'count', 'transacciones_establecimiento'))
    data = data.join(cumulative_compute(data, ['fecha','transaction_id'], ['user_id'], 
                                    'establecimiento', pd.Series.nunique, 'num_establecimientos'))
    data = data.join(cumulative_compute(data, ['fecha','transaction_id'], ['user_id','ciudad'], 
                                    'transaction_id', 'count', 'transacciones_ciudad'))
    data = data.join(cumulative_compute(data, ['fecha','transaction_id'], ['user_id'], 
                                    'ciudad', pd.Series.nunique, 'num_ciudades'))
    data = data.join(cumulative_compute(data, ['fecha','transaction_id'], ['user_id'], 
                                    'monto', 'max', 'monto_maximo'))
    data = data.join(cumulative_compute(data, ['fecha','transaction_id'], ['user_id','dispositivo_marca'], 
                                    'transaction_id', 'count', 'transacciones_marca_dispositivo'))
    data = data.join(cumulative_compute(data, ['fecha','transaction_id'], ['user_id','dispositivo_proveedor'], 
                                    'transaction_id', 'count', 'transacciones_proveedor_dispositivo'))
    data = data.join(cumulative_compute(data, ['fecha','transaction_id'], ['user_id','dispositivo_anio'], 
                                    'transaction_id', 'count', 'transacciones_anio_dispositivo'))
    data = data.join(vectorized_compute(data, ['fecha','transaction_id'], ['user_id'], 
                                    'fecha', 'diff', 'dias_ultima_transaccion').dt.days)
    data = data.merge(vectorized_compute(data, ['fecha','transaction_id'], ['user_id'], 
                                     'fecha', 'min', 'primera_transaccion'),
                  left_on='user_id', right_index=True)
    data['dias_primera_transaccion'] = data[['primera_transaccion','fecha']].diff(axis=1).iloc[:,-1].dt.days
    data = data.join(cumulative_compute(data, ['fecha','transaction_id'], ['user_id'], 
                                    'dispositivo_marca', pd.Series.nunique, 'num_marcas_dispositivo'))
    data = data.join(cumulative_compute(data, ['fecha','transaction_id'], ['user_id'], 
                                    'dispositivo_anio', pd.Series.nunique, 'num_anios_dispositivo'))
    data = data.join(cumulative_compute(data, ['fecha','transaction_id'], ['user_id'], 
                                    'dispositivo_proveedor', pd.Series.nunique, 'num_proveedores_dispositivo'))
    data = data.join(cumulative_compute(data, ['fecha','transaction_id'], ['user_id'], 
                                    'monto', 'mean', 'monto_promedio'))
    data = data.join(cumulative_compute(data, ['fecha','transaction_id'], ['user_id'], 
                                    'monto', 'std', 'monto_dst'))
    data['prop_monto_linea_tc'] = data['monto']/data['linea_tc']
    data['dispositivo'] = data['dispositivo'].astype('str')
    data = data.join(cumulative_compute(data, ['fecha','transaction_id'], ['user_id'], 
                                    'dispositivo', pd.Series.nunique, 'num_dispositivos'))
    
    data['fecha'] = data['fecha'].dt.date.astype(str)

    return data