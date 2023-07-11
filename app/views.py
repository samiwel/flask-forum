from datetime import datetime

from flask import Blueprint, render_template
from .models import Forum, Category

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
def index():
    from .database import db
    data = []
    categories = db.session.query(Category).all()
    for category in categories:
        forums = Forum.query.filter(Forum.category == category).all()
        data.append({
            'category': category.name,
            'forums': [
                {
                    'name': f.name,
                    'description': f.description,
                    'threads': 0,
                    'latest': {
                        'user': 'samiwel',
                        'timestamp': datetime.utcnow()
                    }
                } for f in forums
            ]
        })

    return render_template("page.html", sitename='Zero1', data=data)
