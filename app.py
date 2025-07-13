# app.py

import os
from flask import Flask
from dotenv import load_dotenv

from routes.users import bp as users_bp
from routes.songs import songs_bp
from routes.events import events_bp

load_dotenv()
app = Flask(__name__)

app.register_blueprint(users_bp)
app.register_blueprint(songs_bp)
app.register_blueprint(events_bp)

@app.route("/")
def healthcheck():
    return {
        "status": "OK",
        "service": "Gifted Ministers-Ke Core API",
        "version": "v1"
    }

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("FLASK_ENV") == "development"
    app.run(host="0.0.0.0", port=port, debug=debug)