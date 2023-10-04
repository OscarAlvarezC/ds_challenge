from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class RawData(db.Model):
    __tablename__ = 'production'

    transaction_id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    linea_tc = db.Column(db.Double, nullable=False)
    interes_tc = db.Column(db.Double, nullable=True)
    monto = db.Column(db.Double, nullable=False)
    fecha = db.Column(db.String(50), nullable=False)
    hora = db.Column(db.Integer, nullable=True)
    dispositivo = db.Column(db.String(80), nullable=False)
    establecimiento = db.Column(db.String(50), nullable=True)
    ciudad = db.Column(db.String(50), nullable=True)
    status_txn = db.Column(db.String(50), nullable=False)
    is_prime = db.Column(db.Boolean, nullable=False)
    dcto = db.Column(db.Double, nullable=False)
    cashback = db.Column(db.Integer, nullable=False)


    @classmethod # do not need instanciate a class to use it, similar to static method
    def create(cls, transaction_id, user_id, genero, linea_tc, interes_tc, monto, fecha, hora, dispositivo,
               establecimiento, ciudad, status_txn, is_prime, dcto, cashback):
        eval = RawData(
            transaction_id=transaction_id, 
            user_id=user_id,
            genero=genero,
            linea_tc=linea_tc,
            interes_tc=interes_tc,
            monto=monto,
            fecha=fecha,
            hora=hora,
            dispositivo=dispositivo,
            establecimiento=establecimiento,
            ciudad=ciudad,
            status_txn=status_txn,
            is_prime=is_prime,
            dcto=dcto,
            cashback=cashback
        )
        return eval.save()
    
    def save(self):
        #try:
        db.session.add(self)
        db.session.commit()
        return self
        #except:
        #    return False
        
    def update(self):
        self.save()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False
    
    def json(self):
        return {
            'transaction_id': self.transaction_id,
            'user_id': self.user_id,
            'genero': self.genero,
            'linea_tc': self.linea_tc,
            'interes_tc': self.interes_tc,
            'monto': self.monto,
            'fecha': self.fecha,
            'hora': self.hora,
            'dispositivo': self.dispositivo,
            'establecimiento': self.establecimiento,
            'ciudad': self.ciudad,
            'status_txn': self.status_txn,
            'is_prime': self.is_prime,
            'dcto': self.dcto,
            'cashback': self.cashback
        }
    

class FeatureStore(db.Model):
    __tablename__ = 'feature_store'

    transaction_id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    linea_tc = db.Column(db.Double, nullable=False)
    interes_tc = db.Column(db.Double, nullable=True)
    monto = db.Column(db.Double, nullable=False)
    fecha = db.Column(db.String(50), nullable=False)
    hora = db.Column(db.Integer, nullable=True)
    dispositivo = db.Column(db.String(80), nullable=False)
    establecimiento = db.Column(db.String(50), nullable=True)
    ciudad = db.Column(db.String(50), nullable=True)
    status_txn = db.Column(db.String(50), nullable=False)
    is_prime = db.Column(db.Boolean, nullable=False)
    dcto = db.Column(db.Double, nullable=False)
    cashback = db.Column(db.Integer, nullable=False)
    dispositivo_anio = db.Column(db.Integer, nullable=True)
    dispositivo_marca = db.Column(db.String(50), nullable=True)
    dispositivo_proveedor = db.Column(db.String(50), nullable=True)
    num_transacciones = db.Column(db.Integer, nullable=True)
    transacciones_establecimiento = db.Column(db.Integer, nullable=True)
    num_establecimientos = db.Column(db.Integer, nullable=True)
    transacciones_ciudad = db.Column(db.Integer, nullable=True)
    num_ciudades = db.Column(db.Integer, nullable=True)
    monto_maximo = db.Column(db.Double, nullable=False)
    transacciones_marca_dispositivo = db.Column(db.Integer, nullable=True)
    transacciones_proveedor_dispositivo = db.Column(db.Integer, nullable=True)
    transacciones_anio_dispositivo = db.Column(db.Integer, nullable=True)
    dias_ultima_transaccion = db.Column(db.Integer, nullable=True)
    dias_primera_transaccion = db.Column(db.Integer, nullable=True)
    num_marcas_dispositivo = db.Column(db.Integer, nullable=True)
    num_anios_dispositivo = db.Column(db.Integer, nullable=True)
    num_proveedores_dispositivo = db.Column(db.Integer, nullable=True)
    monto_promedio = db.Column(db.Double, nullable=False)
    monto_dst = db.Column(db.Double, nullable=True)
    prop_monto_linea_tc = db.Column(db.Double, nullable=False)
    num_dispositivos = db.Column(db.Integer, nullable=True)


    @classmethod # do not need instanciate a class to use it, similar to static method
    def create(cls, transaction_id, user_id, genero, linea_tc, interes_tc, monto, fecha, hora, dispositivo,
               establecimiento, ciudad, status_txn, is_prime, dcto, cashback,
               dispositivo_anio, dispositivo_marca, dispositivo_proveedor, num_transacciones, 
               transacciones_establecimiento, num_establecimientos, transacciones_ciudad, num_ciudades, 
               monto_maximo, transacciones_marca_dispositivo, transacciones_proveedor_dispositivo, 
               transacciones_anio_dispositivo, dias_ultima_transaccion,
               dias_primera_transaccion, num_marcas_dispositivo, num_anios_dispositivo, 
               num_proveedores_dispositivo, monto_promedio, monto_dst, prop_monto_linea_tc, 
               num_dispositivos
    ):
        eval = FeatureStore(
            transaction_id=transaction_id, 
            user_id=user_id,
            genero=genero,
            linea_tc=linea_tc,
            interes_tc=interes_tc,
            monto=monto,
            fecha=fecha,
            hora=hora,
            dispositivo=dispositivo,
            establecimiento=establecimiento,
            ciudad=ciudad,
            status_txn=status_txn,
            is_prime=is_prime,
            dcto=dcto,
            cashback=cashback,
            dispositivo_anio=dispositivo_anio,
            dispositivo_marca=dispositivo_marca,
            dispositivo_proveedor=dispositivo_proveedor,
            num_transacciones=num_transacciones,
            transacciones_establecimiento=transacciones_establecimiento,
            num_establecimientos=num_establecimientos,
            transacciones_ciudad=transacciones_ciudad,
            num_ciudades=num_ciudades,
            monto_maximo=monto_maximo,
            transacciones_marca_dispositivo=transacciones_marca_dispositivo,
            transacciones_proveedor_dispositivo=transacciones_proveedor_dispositivo,
            transacciones_anio_dispositivo=transacciones_anio_dispositivo,
            dias_ultima_transaccion=dias_ultima_transaccion,
            dias_primera_transaccion=dias_primera_transaccion,
            num_marcas_dispositivo=num_marcas_dispositivo,
            num_anios_dispositivo=num_anios_dispositivo,
            num_proveedores_dispositivo=num_proveedores_dispositivo,
            monto_promedio=monto_promedio,
            monto_dst=monto_dst,
            prop_monto_linea_tc=prop_monto_linea_tc,
            num_dispositivos=num_dispositivos
        )
        return eval.save()
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
        
    def update(self):
        self.save()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False
    
    def json(self):
        return {
            'transaction_id': self.transaction_id,
            'user_id': self.user_id,
            'genero': self.genero,
            'linea_tc': self.linea_tc,
            'interes_tc': self.interes_tc,
            'monto': self.monto,
            'fecha': self.fecha,
            'hora': self.hora,
            'dispositivo': self.dispositivo,
            'establecimiento': self.establecimiento,
            'ciudad': self.ciudad,
            'status_txn': self.status_txn,
            'is_prime': self.is_prime,
            'dcto': self.dcto,
            'cashback': self.cashback,
            'dispositivo_anio': self.dispositivo_anio,
            'dispositivo_marca': self.dispositivo_marca,
            'dispositivo_proveedor': self.dispositivo_proveedor,
            'num_transacciones': self.num_transacciones,
            'transacciones_establecimiento': self.transacciones_establecimiento,
            'num_establecimientos': self.num_establecimientos,
            'transacciones_ciudad': self.transacciones_ciudad,
            'num_ciudades': self.num_ciudades,
            'monto_maximo': self.monto_maximo,
            'transacciones_marca_dispositivo': self.transacciones_marca_dispositivo,
            'transacciones_proveedor_dispositivo': self.transacciones_proveedor_dispositivo,
            'transacciones_anio_dispositivo': self.transacciones_anio_dispositivo,
            'dias_ultima_transaccion': self.dias_ultima_transaccion,
            'dias_primera_transaccion': self.dias_primera_transaccion,
            'num_marcas_dispositivo': self.num_marcas_dispositivo,
            'num_anios_dispositivo': self.num_anios_dispositivo,
            'num_proveedores_dispositivo': self.num_proveedores_dispositivo,
            'monto_promedio': self.monto_promedio,
            'monto_dst': self.monto_dst,
            'prop_monto_linea_tc': self.prop_monto_linea_tc,
            'num_dispositivos': self.num_dispositivos
        }
    

class ModelDecision(db.Model):
    __tablename__ = 'model_decision'

    transaction_id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    model = db.Column(db.String(16), nullable=False)
    version = db.Column(db.String(16), nullable=False)
    fraud_result = db.Column(db.Boolean, nullable=False)
    fraud_score = db.Column(db.Double, nullable=False)


    @classmethod # do not need instanciate a class to use it, similar to static method
    def create(cls, transaction_id, user_id, model, version, fraud_result, fraud_score):
        eval = ModelDecision(
            transaction_id=transaction_id, 
            user_id=user_id,
            model = model,
            version = version,
            fraud_result = fraud_result,
            fraud_score = fraud_score
        )
        return eval.save()
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
        
    def update(self):
        self.save()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False
    
    def json(self):
        return {
            'transaction_id': self.transaction_id,
            'user_id': self.user_id,
            'model': self.model,
            'version': self.version,
            'fraud_result': self.fraud_result,
            'fraud_score': self.fraud_score
        }

