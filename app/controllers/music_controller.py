from flask import Blueprint, jsonify, request

from app.utils.decorators import jwt_required, roles_required
from app.models.music_model import Musica
from app.views.music_view import musica_lista, musica_detalle

musica_bp = Blueprint("musica", __name__)

@musica_bp.route("/musicas", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_musicas():
    musicas = Musica.get_all()
    return jsonify(musica_lista(musicas))

@musica_bp.route("/musicas/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_musica(id):
    musica = Musica.get_by_id(id)
    if musica:
        return jsonify(musica_detalle(musica))
    return jsonify({"error": "Musica no encontrada"}), 404

@musica_bp.route("/musicas", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_musica():
    data = request.json
    titulo = data.get("titulo")
    artista = data.get("artista")
    duracion = data.get("duracion")
    
    if not titulo or not artista or duracion is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    musica = Musica(titulo=titulo, artista=artista, duracion=duracion)
    musica.save()
    
    return jsonify(musica_detalle(musica)), 201

@musica_bp.route("/musicas/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_musica(id):
    musica = Musica.get_by_id(id)
    
    if not musica:
        return jsonify({"error": "Musica no encontrada"}), 404
    
    data = request.json
    titulo = data.get("titulo")
    artista = data.get("artista")
    duracion = data.get("duracion")
    
    musica.update(titulo=titulo, artista=artista, duracion=duracion)
    
    return jsonify(musica_detalle(musica))
    
@musica_bp.route("/musicas/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_musica(id):
    musica = Musica.get_by_id(id)
    
    if not musica:
        return jsonify({"error": "Musica no encontrada"}), 404
    
    musica.delete()
    return "", 204