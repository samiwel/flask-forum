import datetime

from flask import Flask, render_template
from models import db, Category, Forum

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/samiwelthomas/git/flask-forum/flask-forum.db'
db.init_app(app)

def init_db():
    with app.app_context():
        db.drop_all()
        db.create_all()

        general = Category(name='General')
        cloud = Category(name='Cloud')
        tools = Category(name='DevOps Tools')
        topics = Category(name='Topics')

        db.session.add(general)
        db.session.add(cloud)
        db.session.add(tools)
        db.session.add(topics)
        db.session.commit()
        db.session.add(Forum(name='Introductions', description='Say hello and introduce yourself.', category=general))
        db.session.add(Forum(name='Rules', description='Learn about forum rules and code of conduct', category=general))
        db.session.add(Forum(name='AWS', description='Amazon Web Services', category=cloud))
        db.session.add(Forum(name='Azure', category=cloud))
        db.session.add(Forum(name='GCP', description='Google Cloud Platform', category=cloud))
        db.session.add(Forum(name='Terraform', category=tools))
        db.session.add(Forum(name='Ansible', category=tools))
        db.session.add(Forum(name='Career advice', category=topics))
        db.session.add(Forum(name='Platform Engineering', category=topics))
        db.session.commit()


@app.route("/")
def index():

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
                        'timestamp': datetime.datetime.utcnow()
                    }
                } for f in forums
            ]
        })

    return render_template("page.html", sitename='Zero1', data=data)


if __name__ == '__main__':
    app.run(debug=True)