from model.project import Project
import time

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        self.open_projects_page()
        # init project creation
        self.open_new_project_page()
        self.fill_project_form(project)
        # submit project creation
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        self.open_projects_page()

    def open_projects_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php")):
            wd.get(self.app.base_url + "manage_proj_page.php")

    def open_new_project_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='Create New Project']").click()

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

