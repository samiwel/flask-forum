from app import db, create_app
from app.models import Category, Forum


def init_db():
    app = create_app()
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
