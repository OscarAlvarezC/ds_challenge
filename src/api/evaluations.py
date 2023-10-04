from flask import request, jsonify
from src.models.models import RawData, FeatureStore, ModelDecision
from src.common.utils import HTTPStatus, anyMatchNone, FEATURE_TYPE, THRESHOLD
from src.common.tranform import transform
import pandas as pd
from json import loads, dumps
import os


def configure_evaluation_routes(app):
    
    @app.route('/api/v1/raw_data/<transaction_id>', methods=['GET'])
    def create_evaluation(transaction_id):
        transaction = RawData.query.filter_by(transaction_id=transaction_id).first()
        evaluation = RawData.query.filter_by(user_id=transaction.json().get('user_id')).all()
        result = []
        if evaluation is None:
            return jsonify({'message': 'User does not exists'}), HTTPStatus.NotFound
        for record in evaluation:
            result.append(record.json())
        return jsonify({'transactions': result})
    
    @app.route('/api/v1/compute_features/', methods=['POST'])
    def compute_features():
        json = request.get_json(force=True)
        df = transform(pd.DataFrame(json))
        list_jsons = loads(df.to_json(orient="records"))
        
        for json in list_jsons:
            evaluation = FeatureStore.query.filter_by(transaction_id=json.get('transaction_id')).first()
            if evaluation is None:
                features = FeatureStore.create(
                    transaction_id = json.get('transaction_id'),
                    user_id = json.get('user_id'),
                    genero = json.get('genero'),
                    linea_tc = json.get('linea_tc'),
                    interes_tc = json.get('interes_tc'),
                    monto = json.get('monto'),
                    fecha = json.get('fecha'),
                    hora = json.get('hora'),
                    dispositivo = 1,
                    establecimiento = json.get('establecimiento'),
                    ciudad = json.get('ciudad'),
                    status_txn = json.get('status_txn'),
                    is_prime = json.get('is_prime'),
                    dcto = json.get('dcto'),
                    cashback = json.get('cashback'),
                    dispositivo_anio = json.get('dispositivo_anio'),
                    dispositivo_marca = json.get('dispositivo_marca'),
                    dispositivo_proveedor = json.get('dispositivo_proveedor'),
                    num_transacciones = json.get('num_transacciones'),
                    transacciones_establecimiento = json.get('transacciones_establecimiento'),
                    num_establecimientos = json.get('num_establecimientos'),
                    transacciones_ciudad = json.get('transacciones_ciudad'),
                    num_ciudades = json.get('num_ciudades'),
                    monto_maximo = json.get('monto_maximo'),
                    transacciones_marca_dispositivo = json.get('transacciones_marca_dispositivo'),
                    transacciones_proveedor_dispositivo = json.get('transacciones_proveedor_dispositivo'),
                    transacciones_anio_dispositivo = json.get('transacciones_anio_dispositivo'),
                    dias_ultima_transaccion = json.get('dias_ultima_transaccion'),
                    dias_primera_transaccion = json.get('dias_primera_transaccion'),
                    num_marcas_dispositivo = json.get('num_marcas_dispositivo'),
                    num_anios_dispositivo = json.get('num_anios_dispositivo'),
                    num_proveedores_dispositivo = json.get('num_proveedores_dispositivo'),
                    monto_promedio = json.get('monto_promedio'),
                    monto_dst = json.get('monto_dst'),
                    prop_monto_linea_tc = json.get('prop_monto_linea_tc'),
                    num_dispositivos = json.get('num_dispositivos')
                )
        return jsonify({'features': list_jsons }), HTTPStatus.Created
    

    @app.route('/api/v1/model_decision/<model_segment>/<version>/', methods=['POST'])
    def get_model_decision(model_segment,version):
        model = pd.read_pickle(f'./models/{model_segment}/{version}/clf_lgb.pkl')
        json = request.get_json(force=True)
        list_results = []
        for transaction in json:
            transaction_id = transaction.get('transaction_id')
            user_id = transaction.get('user_id')
            df = pd.json_normalize(transaction)
            df = df.astype(FEATURE_TYPE)
            features = df[['transaction_id'] + model.feature_name_].set_index('transaction_id')
            proba = float(model.predict_proba(features.iloc[[0]])[:,1])
            #list_jsons = loads(df.to_json(orient="records"))
        
            evaluation = ModelDecision.query.filter_by(transaction_id=transaction_id).first()
            if evaluation is None:
                result = ModelDecision.create(
                    transaction_id = transaction_id,
                    user_id = user_id,
                    model = model_segment,
                    version = version,
                    fraud_result = True if proba >= THRESHOLD else False,
                    fraud_score = proba
                )
                list_results.append(result.json())
        return jsonify({'model_decision':  list_results}), HTTPStatus.Created
    
    
    @app.route('/api/v1/model_decision/<transaction_id>/', methods=['GET'])
    def get_score(transaction_id):
        evaluation = ModelDecision.query.filter_by(transaction_id=transaction_id).all()
        result = []
        if evaluation is None:
            return jsonify({'message': 'User does not exists'}), HTTPStatus.NotFound
        for record in evaluation:
            result.append(record.json())
        return jsonify({'evaluations': result})

