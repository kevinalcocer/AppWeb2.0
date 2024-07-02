from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Comercio, Restaurante, Transporte, Hotel

@app.route("/")
def index():
    comercios = Comercio.query.all()
    return render_template('index.html', comercios=comercios)

@app.route("/add", methods=["GET", "POST"])
def add_comercio():
    if request.method == "POST":
        ruc = request.form.get("ruc")
        nombre_comercial = request.form.get("nombre_comercial")
        razon_social = request.form.get("razon_social")
        direccion = request.form.get("direccion")
        telefono = request.form.get("telefono")
        nombre_contacto = request.form.get("nombre_contacto")
        tipo_establecimiento = request.form.get("tipo_establecimiento")
        imagen_logotipo = request.form.get("imagen_logotipo")
        
        if tipo_establecimiento == "restaurante":
            ubicacion = request.form.get("ubicacion")
            fotografia_principal = request.form.get("fotografia_principal")
            direccion_restaurante = request.form.get("direccion_restaurante")
            horario_atencion = request.form.get("horario_atencion")
            especialidad = request.form.get("especialidad")
            rango_precios = request.form.get("rango_precios")
            
            nuevo_comercio = Restaurante(
                ruc=ruc,
                nombre_comercial=nombre_comercial,
                razon_social=razon_social,
                direccion=direccion,
                telefono=telefono,
                nombre_contacto=nombre_contacto,
                tipo_establecimiento=tipo_establecimiento,
                imagen_logotipo=imagen_logotipo,
                ubicacion=ubicacion,
                fotografia_principal=fotografia_principal,
                direccion_restaurante=direccion_restaurante,
                horario_atencion=horario_atencion,
                especialidad=especialidad,
                rango_precios=rango_precios
            )
        elif tipo_establecimiento == "transporte":
            nombre_transporte = request.form.get("nombre_transporte")
            descripcion = request.form.get("descripcion")
            fotografia = request.form.get("fotografia")
            costo_por_hora = request.form.get("costo_por_hora")
            
            nuevo_comercio = Transporte(
                ruc=ruc,
                nombre_comercial=nombre_comercial,
                razon_social=razon_social,
                direccion=direccion,
                telefono=telefono,
                nombre_contacto=nombre_contacto,
                tipo_establecimiento=tipo_establecimiento,
                imagen_logotipo=imagen_logotipo,
                nombre_transporte=nombre_transporte,
                descripcion=descripcion,
                fotografia=fotografia,
                costo_por_hora=costo_por_hora
            )
        elif tipo_establecimiento == "hotel":
            nombre_hotel = request.form.get("nombre_hotel")
            tipo_hotel = request.form.get("tipo_hotel")
            costo = request.form.get("costo")
            ubicacion_geografica = request.form.get("ubicacion_geografica")
            
            nuevo_comercio = Hotel(
                ruc=ruc,
                nombre_comercial=nombre_comercial,
                razon_social=razon_social,
                direccion=direccion,
                telefono=telefono,
                nombre_contacto=nombre_contacto,
                tipo_establecimiento=tipo_establecimiento,
                imagen_logotipo=imagen_logotipo,
                nombre_hotel=nombre_hotel,
                tipo_hotel=tipo_hotel,
                costo=costo,
                ubicacion_geografica=ubicacion_geografica
            )
        else:
            return "Tipo de establecimiento no válido", 400
        
        db.session.add(nuevo_comercio)
        db.session.commit()
        
        return redirect(url_for('index'))
    
    return render_template('add_comercio.html')

@app.route("/edit/<int:comercio_id>", methods=["GET", "POST"])
def edit_comercio(comercio_id):
    comercio = Comercio.query.get_or_404(comercio_id)
    
    if request.method == "POST":
        comercio.ruc = request.form.get("ruc")
        comercio.nombre_comercial = request.form.get("nombre_comercial")
        comercio.razon_social = request.form.get("razon_social")
        comercio.direccion = request.form.get("direccion")
        comercio.telefono = request.form.get("telefono")
        comercio.nombre_contacto = request.form.get("nombre_contacto")
        comercio.tipo_establecimiento = request.form.get("tipo_establecimiento")
        comercio.imagen_logotipo = request.form.get("imagen_logotipo")
        
        if isinstance(comercio, Restaurante):
            comercio.ubicacion = request.form.get("ubicacion")
            comercio.fotografia_principal = request.form.get("fotografia_principal")
            comercio.direccion_restaurante = request.form.get("direccion_restaurante")
            comercio.horario_atencion = request.form.get("horario_atencion")
            comercio.especialidad = request.form.get("especialidad")
            comercio.rango_precios = request.form.get("rango_precios")
        elif isinstance(comercio, Transporte):
            comercio.nombre_transporte = request.form.get("nombre_transporte")
            comercio.descripcion = request.form.get("descripcion")
            comercio.fotografia = request.form.get("fotografia")
            comercio.costo_por_hora = request.form.get("costo_por_hora")
        elif isinstance(comercio, Hotel):
            comercio.nombre_hotel = request.form.get("nombre_hotel")
            comercio.tipo_hotel = request.form.get("tipo_hotel")
            comercio.costo = request.form.get("costo")
            comercio.ubicacion_geografica = request.form.get("ubicacion_geografica")
        
        db.session.commit()
        
        return redirect(url_for('index'))
    
    return render_template('edit_comercio.html', comercio=comercio)

@app.route("/delete/<int:comercio_id>", methods=["POST"])
def delete_comercio(comercio_id):
    comercio = Comercio.query.get_or_404(comercio_id)
    db.session.delete(comercio)
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route("/view/<int:comercio_id>", methods=["GET"])
def view_comercio(comercio_id):
    comercio = Comercio.query.get_or_404(comercio_id)
    return render_template('view_comercio.html', comercio=comercio)
