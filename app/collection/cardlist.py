from flask import Blueprint

from app.model.card import Card
from app.authentication.auth import login_required

bp = Blueprint('collection', __name__)


@bp.route('/')
@login_required
def index(id):
    Card.query.filter_by(Card.user.id)
