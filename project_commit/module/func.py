from flask import jsonify
import app


# helpers
def scheme_project(row):
    commits = []
    for commit in row.commits:
        commits.append(scheme_commit(commit))

    return {
        'id': row.id,
        'name': row.name,
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
        'user_id': row.user_id,
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
    # project
    new_project_one = app.Project(name='114 Big freaking building', client_id=1)
    new_project_two = app.Project(name='255 shacksville', expired=True, client_id=2)
    new_project_three = app.Project(name='255 shacksville', expired=True, client_id=2)

    db.session.add(new_project_one)
    db.session.add(new_project_two)
    db.session.add(new_project_three)

    # user
    new_user_one = app.User(name='Dave Dave')
    new_user_two = app.User(name='Nigel Nigel')
    new_user_three = app.User(name='Billy Billy')

    db.session.add(new_user_one)
    db.session.add(new_user_two)
    db.session.add(new_user_three)

    # client
    new_client_one = app.Client(name='Howdy Hughes')
    new_client_two = app.Client(name='Divided')
    new_client_three = app.Client(name='Gang of four')

    db.session.add(new_client_one)
    db.session.add(new_client_two)
    db.session.add(new_client_three)

    # commit
    new_commit_one = app.Commit(working_files='project files', deliverable='deliv_01_.jpg', expired=False, commit_type='deliverable', user_id=1, project_id=1)
    new_commit_two = app.Commit(working_files='project files', deliverable='deliv_01_.jpg', expired=False, commit_type='comment', user_id=2, project_id=1)
    new_commit_three = app.Commit(working_files='project files', deliverable='deliv_02_.jpg', expired=False, commit_type='deliverable', user_id=3, project_id=1)
    new_commit_four = app.Commit(working_files='project files', deliverable='project handoffs', expired=False, commit_type='comment', user_id=2, project_id=2)
    new_commit_five = app.Commit(working_files='project files', deliverable='project handoffs', expired=True, commit_type='reference', user_id=3, project_id=1)
    new_commit_six = app.Commit(working_files='project files', deliverable='bla bla', expired=True, commit_type='comment', user_id=2, project_id=1)

    db.session.add(new_commit_one)
    db.session.add(new_commit_two)
    db.session.add(new_commit_three)
    db.session.add(new_commit_four)
    db.session.add(new_commit_five)

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
