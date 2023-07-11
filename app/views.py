import hashlib
from datetime import datetime

from flask import Blueprint, render_template, request, redirect, session, url_for
from .models import Forum, Category, User

main_blueprint = Blueprint("main", __name__)

def hash_plaintext_password(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()

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

    return render_template("page.html", sitename='Forums', data=data)


@main_blueprint.route("/signup", methods=['GET'])
def get_signup():
    return render_template("signup.html")

@main_blueprint.route("/signup", methods=['POST'])
def post_signup():
    form_data = request.form

    from .models import User
    password_hash = hash_plaintext_password(form_data.get('password'))
    new_user = User(real_name=form_data.get('full_name'), username=form_data.get('username'), email=form_data.get('email'), password=password_hash)

    from .database import db
    db.session.add(new_user)
    db.session.commit()

    return redirect("/signup")

@main_blueprint.route("/signin", methods=['GET'])
def get_signin():
    return render_template("signin.html")

@main_blueprint.route("/signin", methods=['POST'])
def post_signin():
    form_data = request.form

    username = form_data.get('username')
    password = hash_plaintext_password(form_data.get('password'))

    from .database import db
    user = db.session.query(User).filter_by(username=username, password=password).first()

    if user:
        session['user_id'] = user.id

    return redirect(url_for('main.index'))

@main_blueprint.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('main.index'))