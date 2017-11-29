import datetime
import sqlite3

from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

import module.func


# slite3 database stuff
SQLITE_DATABASE = 'temp_db.db'
conn = sqlite3.connect(SQLITE_DATABASE)
conn.close()

# flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///temp_db.db'

#flask-sqlalchemy
db = SQLAlchemy(app)

# models

# TODO:
## commit types
## reference, comment, deliverable


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    projects = db.relationship('Project',
        backref=db.backref('Clients', lazy=True))

    def __repr__(self):
        return '<Client %r>' % self.id


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    expired = db.Column(db.Boolean, default=False)

    client_id = db.Column(db.Integer, db.ForeignKey('client.id'),
        nullable=False)

    commits = db.relationship('Commit',
        backref=db.backref('Project', lazy=True))


    def __repr__(self):
        return '<Project %r>' % self.id


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    picture = db.Column(db.String, default='default_user.jpg')

    commits = db.relationship('Commit',
        backref=db.backref('User', lazy=True))

    # lead:[PROJECT:ID]

    def __repr__(self):
        return '<User %r>' % self.id


class Commit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    working_files = db.Column(db.String)
    deliverable = db.Column(db.String)
    subdate = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    commit_type = db.Column(db.String)
    commit_round = db.Column(db.Integer, default=1)
    expired = db.Column(db.Boolean, default=False)
    note = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'),
        nullable=False)

    def __repr__(self):
        return '<Commit %r>' % self.id


# create tables
db.create_all()

@app.route('/')
def index():
    # module.func.populate_db(db)
    data = {
        'client': module.func.client_get(1),
        'clients': module.func.client_all(),
        'user': module.func.user_get(1),
        'users': module.func.user_all(),
        'project': module.func.project_get(1),
        'projects': module.func.project_all(),
        'commit': module.func.commit_get(1),
        'commits': module.func.commit_all()
    }

    return render_template('index.html', data=data)


@app.route('/client')
def clients():
    data = module.func.client_all()

    return render_template('clients.html', data=data)


@app.route('/project')
def projects():
    data = module.func.project_all()

    return render_template('projects.html', data=data)


@app.route('/user')
def users():
    data = module.func.user_all()

    return render_template('users.html', data=data)


@app.route('/commit')
def commits():
    data = module.func.commit_all()

    return render_template('commits.html', data=data)


@app.route('/client/<int:id>')
def client(id):
    data = module.func.client_get(id)

    # relational data
    # projects
    projects = []
    for project in data[0]['projects']:
        raw_project = Project.query.filter_by(id=project.id).first()
        projects.append(module.func.scheme_project(raw_project))

    data[0]['projects'] = projects


    return render_template('client.html', data=data)


@app.route('/project/<int:id>')
def project(id):
    # get base project data
    data = module.func.project_get(id)

    # append relational
    # commits
    commits = []
    user_ids = []
    users = []
    for commit in data[0]['commits']:
        raw_commit = Commit.query.filter_by(id=commit.id).first()
        commits.append(module.func.scheme_commit(raw_commit))

    data[0]['commits'] = commits

    # user (only works if commits have been processed)
    for user in data[0]['commits']:
        if user['user_id'] not in user_ids:
            user_ids.append(user['user_id'])
            
            raw_user = User.query.filter_by(id=user['user_id']).first()
            if raw_user != None:
                users.append(module.func.scheme_user(raw_user))

    data[0]['users'] = users

    # commit
    # add replace commit:user_id with scheme_user()
    for commit in data[0]['commits']:
        if commit['user_id'] in user_ids:
            for user in data[0]['users']:
                if user['id'] == commit['user_id']:
                    commit['user_id'] = {'id': user['id'], 'name': user['name']}

    # client
    client = {}
    raw_client = Client.query.filter_by(id=data[0]['client_id']).first()
    if raw_client:
         data[0]['client_id'] = module.func.scheme_client(raw_client)


    return render_template('project.html', data=data)


@app.route('/user/<int:id>')
def user(id):
    # user data
    data = module.func.user_get(id)

    # append relational
    # commits
    commits = []
    project_ids = []
    projects = []
    for commit in data[0]['commits']:
        raw_commit = Commit.query.filter_by(id=commit.id).first()
        commits.append(module.func.scheme_commit(raw_commit))

    data[0]['commits'] = commits

    # projects (only works if commits have been processed)
    for commit in data[0]['commits']:
        if commit['project_id'] not in project_ids:
            project_ids.append(commit['project_id'])
            raw_project = Project.query.filter_by(id=commit['project_id']).first()
            if raw_project != None:
                projects.append(module.func.scheme_project(raw_project))

    data[0]['projects'] = projects


    return render_template('user.html', data=data)


@app.route('/commit/<int:id>')
def commit(id):
    data = module.func.commit_get(id)

    # append relational
    # user
    user = {}
    raw_user = User.query.filter_by(id=data[0]['user_id']).first()
    if raw_user:
         data[0]['user_id'] = module.func.scheme_user(raw_user)

    # project
    project = {}
    raw_project = Project.query.filter_by(id=data[0]['project_id']).first()
    if raw_project:
        data[0]['project_id'] = module.func.scheme_project(raw_project)


    return render_template('commit.html', data=data)


"""
@app.route('/_get_current_user')
def get_current_user():
    return jsonify(username=g.user.username,
                   email=g.user.email,
                   id=g.user.id)
"""

if __name__ == "__main__":
    # app = create_app(config.DATABASE_URI, debug=True)
    app.run(debug=True)