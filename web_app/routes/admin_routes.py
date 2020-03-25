# web_app/routes/admin_routes.py

from flask import Blueprint, jsonify, request, render_template, flash, redirect
from web_app.models import db
from web_app.routes.twitter_routes import store_twitter_user_data

admin_routes = Blueprint("amdmin_routes", __name__)

# ideally be password protected
@admin_routes.route("/admin/db/reset")
def reset_db():
    print(type(db))
    db.drop_all()
    db.create_all()
    return jsonify({"message": "DEB RESET OK"})

@admin_routes.route("/admin/db/seed")
def seed_db():
    print(type(db))
    default_users = ["elonmusk", "s2t2", "austen", "nbcnews", "exjon", "neontaster", "comfortablysmug"]
    for screen_name in default_users:
        db_user, statues = store_twitter_user_data(screen_name)

    return jsonify({"message": f"DB SEEDED OK (w/ {len(default_users)})"})
