import os
from flask import jsonify, render_template
from . import app
from .pokeneas import obtener_pokenea_aleatorio

@app.route('/api/pokenea', methods=['GET'])
def get_pokenea():
    pokenea = obtener_pokenea_aleatorio()
    response = {
        "id": pokenea["id"],
        "nombre": pokenea["nombre"],
        "altura": pokenea["altura"],
        "habilidad": pokenea["habilidad"],
        "imagen": pokenea["imagen"],
        "frase_filosofica": pokenea["frase_filosofica"],
        "contenedor_id": os.getenv('CONTAINER_ID', 'default_container')
    }
    return jsonify(response)

@app.route('/display', methods=['GET'])
def display_pokenea():
    pokenea = obtener_pokenea_aleatorio()
    return render_template('display.html', pokenea=pokenea, contenedor_id=os.getenv('CONTAINER_ID', 'default_container'))
