import random

from flask import jsonify

import app
import module.fake_data


# helpers
def scheme_project(row):
    commits = []
    client = {}
    for commit in row.commits:
        commits.append(scheme_commit(commit))

    raw_client = app.Client.query.filter_by(id=row.client_id).first()
    if raw_client:
        client = {
            'id': raw_client.id,
            'name': raw_client.name
        }
        
    return {
        'id': row.id,
        'name': row.name,
        'expired': row.expired,
        'client_id': client,
        'commits': commits
    }


def scheme_user(row, basic=False):
    if basic == False:
        commits = []
        for commit in row.commits:
            commits.append(scheme_commit(commit))

        return {
            'id': row.id,
            'name': row.name,
            'commits': commits,
            'picture': row.picture
        }
    else:
        return {
            'id': row.id,
            'name': row.name,
            'picture': row.picture
        }


def scheme_commit(row):
    # get user
    user_row = app.User.query.filter_by(id=row.user_id).first()
    user = {
        'id': user_row.id,
        'name': user_row.name,
        'picture': user_row.picture
    }
    # get project
    project = {}
    project_row = app.Project.query.filter_by(id=row.project_id).first()
    
    if project_row != None:
        project = {
            'id': project_row.id,
            'name': project_row.name,
            'expired': project_row.expired,
        }

    return {
        'id': row.id,
        'working_files': row.working_files,
        'deliverable': row.deliverable,
        'project_id': project,
        'user_id': user,
        'subdate': row.subdate,
        'commit_type': row.commit_type,
        'commit_round': row.commit_round,
        'expired': row.expired
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
            commit_round=random.choice([1, 2, 3])
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
