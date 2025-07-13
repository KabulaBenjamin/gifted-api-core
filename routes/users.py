# routes/users.py

from flask import Blueprint, jsonify, g, request
from supabase_client import supabase
from auth import jwt_required

bp = Blueprint("users", __name__, url_prefix="/api/v1/users")


@bp.route("/me", methods=["GET"])
@jwt_required
def get_current_user():
    response = supabase.table("users").select("*").eq("id", g.user_id).single().execute()
    if response.error:
        return jsonify({"error": response.error.message}), 404
    return jsonify(response.data), 200


@bp.route("/me", methods=["PATCH"])
@jwt_required
def update_current_user():
    updates = request.get_json()
    response = supabase.table("users").update(updates).eq("id", g.user_id).execute()
    if response.error:
        return jsonify({"error": response.error.message}), 400
    return jsonify(response.data), 200
