from app import db

class Comercio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ruc = db.Column(db.String(20), unique=True, nullable=False)
    nombre_comercial = db.Column(db.String(50), nullable=False)
    razon_social = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    nombre_contacto = db.Column(db.String(50), nullable=False)
    tipo_establecimiento = db.Column(db.String(20), nullable=False)
    imagen_logotipo = db.Column(db.String(100), nullable=True)
    __mapper_args__ = {
        'polymorphic_identity': 'comercio',
        'polymorphic_on': tipo_establecimiento
    }

class Restaurante(Comercio):
    id = db.Column(db.Integer, db.ForeignKey('comercio.id'), primary_key=True)
    ubicacion = db.Column(db.String(100))
    fotografia_principal = db.Column(db.String(100))
    direccion_restaurante = db.Column(db.String(100))
    horario_atencion = db.Column(db.String(50))
    especialidad = db.Column(db.String(50))
    rango_precios = db.Column(db.String(50))
    __mapper_args__ = {
        'polymorphic_identity': 'restaurante',
    }

class Transporte(Comercio):
    id = db.Column(db.Integer, db.ForeignKey('comercio.id'), primary_key=True)
    nombre_transporte = db.Column(db.String(50))
    descripcion = db.Column(db.String(100))
    fotografia = db.Column(db.String(100))
    costo_por_hora = db.Column(db.Float)
    __mapper_args__ = {
        'polymorphic_identity': 'transporte',
    }

class Hotel(Comercio):
    id = db.Column(db.Integer, db.ForeignKey('comercio.id'), primary_key=True)
    nombre_hotel = db.Column(db.String(50))
    tipo_hotel = db.Column(db.String(50))
    costo = db.Column(db.Float)
    ubicacion_geografica = db.Column(db.String(100))
    __mapper_args__ = {
        'polymorphic_identity': 'hotel',
    }
