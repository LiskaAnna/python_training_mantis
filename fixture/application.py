from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.james import JamesHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper
from fixture.soap import SoapHelper



class Application:

    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognised browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.james = JamesHelper(self)
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)
        self.soap = SoapHelper(self)
        self.config = config
        self.base_url = config['web']['baseUrl']
        self.login = config['webadmin']['username']
        self.password = config['webadmin']['password']

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)
        return wd

    def open_login_page(self):
        wd = self.wd
        wd.get(self.base_url + "login_page.php")
        return wd

    def destroy(self):
        self.wd.quit()

    def return_to_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("group")) > 0):
            wd.find_element_by_link_text("home page").click()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
