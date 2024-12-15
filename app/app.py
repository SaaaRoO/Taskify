from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from db.database import db
from routes.auth_routes import auth_bp
from routes.task_routes import task_bp

app = Flask(__name__)
app.config.from_object(Config)

# build JWT & SQLAlchemy
db.init_app(app)
jwt = JWTManager(app)


app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(task_bp, url_prefix="/api")

# create tables
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
