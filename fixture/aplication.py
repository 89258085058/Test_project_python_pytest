from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Aplication:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php?selected%5B%5D=1&delete=Delete+group%28s%29")

    def destroy(self):
        self.wd.quit()


