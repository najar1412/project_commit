from flask import jsonify
import app


# helpers
def scheme_project(row):
    commits = []
    for commit in row.commits:
        commits.append(scheme_commit(commit))

    return {
        'id': row.id,
        'expired': row.expired,
        'client_id': row.client_id,
        'commits': commits
    }


def scheme_user(row):

    commits = []
    for commit in row.commits:
        commits.append(scheme_commit(commit))

    return {
        'id': row.id,
        'name': row.name,
        'commits': commits
    }


def scheme_commit(row):
    
    return {
        'id': row.id,
        'working_files': row.working_files,
        'deliverable': row.deliverable,
        'project_id': row.project_id,
        'user_id': row.user_id
    }


def scheme_client(row):
    projects = []
    for project in row.projects:
        projects.append(scheme_project(project))

    return {
        'id': row.id,
        'name': row.name,
        'projects': projects
    }


def populate_db(db):
    # project
    new_project = app.Project(expired='expiring soon', client_id=1)
    # user
    new_user = app.User(name='new name')
    # client
    new_client = app.Client(name='new client')
    # commit
    new_commit = app.Commit(working_files='project files', deliverable='project handoffs', user_id=1, project_id=1)

    db.session.add(new_project)
    db.session.add(new_user)
    db.session.add(new_client)
    db.session.add(new_commit)

    db.session.commit()


def project_get(id):
    row = app.Project.query.filter_by(id=id).first()

    if row != None:
        output = []
        x = scheme_project(row)
        output.append(x)

        return output

    return []


def user_get(id):
    row = app.User.query.filter_by(id=id).first()

    if row != None:
        output = []
        x = scheme_user(row)
        output.append(x)

        return output

    return []


def commit_get(id):
    row = app.Commit.query.filter_by(id=id).first()

    if row != None:
        output = []
        x = scheme_commit(row)

        output.append(x)

        return output

    return []


def client_get(id):
    row = app.Client.query.filter_by(id=id).first()

    if row != None:
        output = []
        x = scheme_client(row)
        output.append(x)

        return output

    return []


def project_all():
    output = []
    rows = app.Project.query.all()
    for row in rows:
        x = scheme_project(row)
        output.append(x)

    return output


def user_all():
    output = []
    rows = app.User.query.all()
    for row in rows:
        x = scheme_user(row)
        output.append(x)

    return output


def commit_all():
    output = []
    rows = app.Commit.query.all()
    for row in rows:
        x = scheme_commit(row)

        output.append(x)

    return output


def client_all():
    output = []
    rows = app.Client.query.all()
    for row in rows:
        x = scheme_client(row)
        output.append(x)

    return output
