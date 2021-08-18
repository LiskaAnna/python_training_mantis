import mysql.connector
from model.project import Project


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_projects_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, name, description from mantis_project_table")
            for row in cursor:
                (id, name, description) = row
                list.append(Project(id=str(id), name=name, description=description))
        finally:
            cursor.close()
        return list

    def check_name(self, project_name):
        cursor = self.connection.cursor()
        query = "select count(*) as count from mantis_project_table where name = '" + project_name + "'"
        try:
            cursor.execute(query)
            for row in cursor:
                (count) = row
        finally:
            cursor.close()
        return count[0] > 0

    def destroy(self):
        self.connection.close()
