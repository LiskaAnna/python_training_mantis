from model.project import Project
import generator.project


def test_add_project(app, db, json_projects):
     app.session.login_if_needed()
     project = json_projects
     if db.check_name(project.name):
          project.name = generator.project.random_string(project.name, 5)
     old_projects = app.soap.get_projects(app.login, app.password)
     app.project.create(project)
     new_projects = app.soap.get_projects(app.login, app.password)
     old_projects.append(project)
     assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
