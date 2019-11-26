from flask import Flask
from .pnw_makes.views import views_bp

app = Flask(__name__)

app.register_blueprint(views_bp, url_prefix='/')

if __name__ == "__main__":
    app.run()