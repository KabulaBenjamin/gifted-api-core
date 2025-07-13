# routes/events.py

from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from supabase_client import supabase
from auth import jwt_required, roles_required
from models.events import EventCreate, EventUpdate

events_bp = Blueprint("events", __name__, url_prefix="/api/v1/events")

@events_bp.route("", methods=["GET"])
def list_events():
    resp = supabase.table("events").select("*").execute()
    return jsonify(resp.data), 200

@events_bp.route("/<int:event_id>", methods=["GET"])
def get_event(event_id):
    resp = supabase.table("events").select("*").eq("id", event_id).single().execute()
    if resp.error or not resp.data:
        return jsonify({"error": "Event not found"}), 404
    return jsonify(resp.data), 200

@events_bp.route("", methods=["POST"])
@jwt_required
@roles_required("admin")
def create_event():
    try:
        payload = EventCreate(**request.get_json())
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 422

    resp = supabase.table("events").insert(payload.dict()).single().execute()
    if resp.error:
        return jsonify({"error": resp.error.message}), 400
    return jsonify(resp.data), 201

@events_bp.route("/<int:event_id>", methods=["PATCH"])
@jwt_required
@roles_required("admin")
def update_event(event_id):
    try:
        payload = EventUpdate(**request.get_json())
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 422

    data = payload.dict(exclude_none=True)
    resp = supabase.table("events").update(data).eq("id", event_id).single().execute()
    if resp.error:
        return jsonify({"error": resp.error.message}), 400
    return jsonify(resp.data), 200

@events_bp.route("/<int:event_id>", methods=["DELETE"])
@jwt_required
@roles_required("admin")
def delete_event(event_id):
    resp = supabase.table("events").delete().eq("id", event_id).single().execute()
    if resp.error:
        return jsonify({"error": resp.error.message}), 400
    return jsonify({"id": event_id}), 200