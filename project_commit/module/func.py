from flask import jsonify
import app


def project_get(id):
    row = app.Project.query.filter_by(id=id).first()

    if row != None:
        output = []
        x = {
            'id': row.id,
            'expired': row.expired,
            'client_id': row.client_id,
            'commits': row.commits
        }
        output.append(x)

        return output

    return []


def user_get(id):
    row = app.User.query.filter_by(id=id).first()

    if row != None:
        output = []
        x = {
            'id': row.id,
            'name': row.name,
            'commits': row.commits
        }
        output.append(x)

        return output

    return []


def commit_get(id):
    row = app.Commit.query.filter_by(id=id).first()

    if row != None:
        output = []

        x = {
            'id': row.id,
            'working_files': row.working_files,
            'deliverable': row.deliverable,
            'project_id': row.project_id,
            'user_id': row.user_id
        }
        output.append(x)

        return output

    return []


def client_get(id):
    row = app.Client.query.filter_by(id=id).first()

    if row != None:
        output = []

        x = {
            'id': row.id,
            'name': row.name,
            'projects': row.projects
        }
        output.append(x)

        return output

    return []


def project_all():
    output = []
    rows = app.Project.query.all()
    for row in rows:
        x = {
            'id': row.id,
            'expired': row.expired,
            'client_id': row.client_id,
            'commits': row.commits
        }
        output.append(x)

    return output


def user_all():
    output = []
    rows = app.User.query.all()
    for row in rows:
        x = {
            'id': row.id,
            'name': row.name,
            'commits': row.commits
        }
        output.append(x)

    return output


def commit_all():
    output = []
    rows = app.Commit.query.all()
    for row in rows:
        x = {
            'id': row.id,
            'working_files': row.working_files,
            'deliverable': row.deliverable,
            'project_id': row.project_id,
            'user_id': row.user_id
        }
        output.append(x)

    return output


def client_all():
    output = []
    rows = app.Client.query.all()
    for row in rows:
        x = {
            'id': row.id,
            'name': row.name,
            'projects': row.projects
        }
        output.append(x)

    return output
