import datetime

from flask import Flask, render_template
from app.models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask-forum.db'
db.init_app(app)


@app.route("/")
def index():

    data = [
        {
            "category": "general",
            "forums": [
                {
                    "name": "Meet and greet",
                    "description": "Say hello and introduce yourself.",
                    "threads": 20,
                    "latest": {
                        "user": "samiwel",
                        "timestamp": datetime.datetime.utcnow()
                    }
                }
            ]
        },
        {
            "category": "cloud",
            "forums": [
                {
                    "name": "AWS",
                    "description": "Amazon Web Services",
                    "threads": 100,
                    "latest": {
                        "user": "samiwel",
                        "timestamp": datetime.datetime.utcnow()
                    }
                },
                {
                    "name": "Azure",
                    "description": "",
                    "threads": 57,
                    "latest": {
                        "user": "samiwel",
                        "timestamp": datetime.datetime.utcnow()
                    }
                },
                {
                    "name": "GCP",
                    "description": "Google Cloud Platform",
                    "threads": 30,
                    "latest": {
                        "user": "samiwel",
                        "timestamp": datetime.datetime.utcnow()
                    }
                }
            ]
        },
        {
            "category": "DevOps",
            "forums": [
                {
                    "name": "DevOps",
                    "description": "",
                    "threads": 100,
                    "latest": {
                        "user": "samiwel",
                        "timestamp": datetime.datetime.utcnow()
                    }
                },
                {
                    "name": "Platform Engineering",
                    "description": "",
                    "threads": 120,
                    "latest": {
                        "user": "samiwel",
                        "timestamp": datetime.datetime.utcnow()
                    }
                },
                {
                    "name": "Terraform",
                    "description": "",
                    "threads": 300,
                    "latest": {
                        "user": "samiwel",
                        "timestamp": datetime.datetime.utcnow()
                    }
                },
                {
                    "name": "Ansible",
                    "description": "",
                    "threads": 200,
                    "latest": {
                        "user": "samiwel",
                        "timestamp": datetime.datetime.utcnow()
                    }
                }
            ]
        }
    ]


    return render_template("page.html", sitename='Zero1', data=data)


if __name__ == '__main__':
    app.run(debug=True)