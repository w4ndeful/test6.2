from flask import Blueprint

posts_bp = Blueprint("posts", __name__, static_folder="static", template_folder="templates")

from . import views
