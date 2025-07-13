# routes/songs.py

from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from supabase_client import supabase
from auth import jwt_required, roles_required
from models.songs import SongCreate, SongUpdate

songs_bp = Blueprint("songs", __name__, url_prefix="/api/v1/songs")

@songs_bp.route("", methods=["GET"])
def list_songs():
    resp = supabase.table("songs").select("*").execute()
    return jsonify(resp.data), 200

@songs_bp.route("/<int:song_id>", methods=["GET"])
def get_song(song_id):
    resp = supabase.table("songs").select("*").eq("id", song_id).single().execute()
    if resp.error or not resp.data:
        return jsonify({"error": "Song not found"}), 404
    return jsonify(resp.data), 200

@songs_bp.route("", methods=["POST"])
@jwt_required
@roles_required("admin")
def create_song():
    try:
        payload = SongCreate(**request.get_json())
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 422

    resp = supabase.table("songs").insert(payload.dict()).single().execute()
    if resp.error:
        return jsonify({"error": resp.error.message}), 400
    return jsonify(resp.data), 201

@songs_bp.route("/<int:song_id>", methods=["PATCH"])
@jwt_required
@roles_required("admin")
def update_song(song_id):
    try:
        payload = SongUpdate(**request.get_json())
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 422

    data = payload.dict(exclude_none=True)
    resp = supabase.table("songs").update(data).eq("id", song_id).single().execute()
    if resp.error:
        return jsonify({"error": resp.error.message}), 400
    return jsonify(resp.data), 200

@songs_bp.route("/<int:song_id>", methods=["DELETE"])
@jwt_required
@roles_required("admin")
def delete_song(song_id):
    resp = supabase.table("songs").delete().eq("id", song_id).single().execute()
    if resp.error:
        return jsonify({"error": resp.error.message}), 400
    return jsonify({"id": song_id}), 200