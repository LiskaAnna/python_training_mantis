from model.project import Project
import random


def test_delete_some_project(app, db):
    if not app.session.is_logged_in():
        app.session.login("administrator", "root")
    if len(db.get_projects_list()) == 0:
        app.project.create(Project(name="test"))
    old_projects = db.get_projects_list()
    project = random.choice(old_projects)
    print(project)
    app.project.delete_project_by_id(project.id)
    new_projects = db.get_projects_list()
    old_projects.remove(project)
    assert old_projects == new_projects
