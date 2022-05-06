from flask import Blueprint


bp = Blueprint('auths', __name__, template_folder='auths', url_prefix='/')

from app.blueprints.auths import routes

