from flask import Blueprint, render_template

views_bp = Blueprint('views_bp', __name__,
    template_folder='templates', static_folder='pnw_makes/static')


@views_bp.route('/')
def hello_world():
    return render_template('home.html');
