from model.project import Project
import random


def test_delete_some_project(app, db):
    app.session.login_if_needed()
    if len(db.get_projects_list()) == 0:
        app.project.create(Project(name="test"))
    old_projects = app.soap.get_projects(app.login, app.password)
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = app.soap.get_projects(app.login, app.password)
    old_projects.remove(project)
    assert old_projects == new_projects
