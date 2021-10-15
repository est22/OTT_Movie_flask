import os

from flask import Flask, send_from_directory, jsonify, render_template, request

from server.landing import landing as landing_bp
from server.api import api as api_bp

app = Flask(__name__, static_folder="../client/build")
app.register_blueprint(landing_bp, url_prefix="/landing")
app.register_blueprint(api_bp, url_prefix="/api/v1")


@app.route("/")
def serve():
    """serves React App"""
    return send_from_directory(app.static_folder, "index.html")


@app.route("/<path:path>")
def static_proxy(path):
    """static folder serve"""
    file_name = path.split("/")[-1]
    dir_name = os.path.join(app.static_folder, "/".join(path.split("/")[:-1]))
    return send_from_directory(dir_name, file_name)


@app.errorhandler(404)
def handle_404(e):
    if request.path.startswith("/api/"):
        return jsonify(message="Resource not found"), 404
    return send_from_directory(app.static_folder, "index.html")


@app.errorhandler(405)
def handle_405(e):
    if request.path.startswith("/api/"):
        return jsonify(message="Mehtod not allowed"), 405
    return e
