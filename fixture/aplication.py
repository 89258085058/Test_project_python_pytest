from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.manager import ManagerHelper
from selenium.webdriver.support.ui import Select

class Aplication:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.manager = ManagerHelper(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/birthdays.php")

    def destroy(self):
        self.wd.quit()


