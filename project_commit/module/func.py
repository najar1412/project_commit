import random

from flask import jsonify

import app
import module.fake_data


# helpers
def scheme_project(row):
    return {
        'id': row.id,
        'name': row.name,
        'expired': row.expired,
        'client_id': row.client_id,
        'commits': row.commits
    }


def scheme_user(row):
    return {
        'id': row.id,
        'name': row.name,
        'commits': row.commits,
        'picture': row.picture
    }


def scheme_commit(row):
    return {
        'id': row.id,
        'working_files': row.working_files,
        'deliverable': row.deliverable,
        'project_id': row.project_id,
        'user_id':row.user_id,
        'subdate': row.subdate,
        'commit_type': row.commit_type,
        'commit_round': row.commit_round,
        'expired': row.expired,
        'note': row.note
    }


def scheme_client(row):
    return {
        'id': row.id,
        'name': row.name,
        'projects': row.projects
    }


def populate_db(db):
    # user
    num_of_users = 5
    for x in range(num_of_users):
        new_user = app.User(name=module.fake_data.user_name(), picture=module.fake_data.user_jpg())
        db.session.add(new_user)
    db.session.commit()

    # client
    num_of_clients = 10
    for x in range(num_of_clients):
        new_client = app.Client(name=module.fake_data.client_name())
        db.session.add(new_client)

    # project
    num_of_projects = 6
    for x in range(num_of_projects):
        new_project = app.Project(
            name=module.fake_data.project_name(),
            expired=random.choice([True, False]), 
            client_id=random.choice(range(num_of_clients))
        )
        db.session.add(new_project)

    # commit
    num_of_commits = 30
    for x in range(num_of_commits):
        new_commit = app.Commit(
            working_files='project files', 
            deliverable=module.fake_data.populate_jpg(), 
            expired=random.choice([True, False, False]), 
            commit_type=random.choice(['reference', 'comment', 'deliverable']), 
            user_id=random.choice([1, 2, 3, 4, 5]), 
            project_id=random.choice(range(num_of_projects)),
            commit_round=random.choice([1, 2, 3]),
            note=module.fake_data.commit_note()
        )
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
