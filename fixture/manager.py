from model.contact import Contact

class ManagerHelper:

    def __init__(self, app):
        self.app = app


    def add_personal_information(self, contact):
        wd = self.app.wd
        self.add_new_contact()
        self.entering_personal_information(contact, wd)
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()

    def entering_personal_information(self, contact, wd):
        self.change_value_contact("firstname", contact.firstname)
        self.change_value_contact("middlename", contact.middlename)
        self.change_value_contact("lastname", contact.lastname)
        self.change_value_contact("nickname", contact.nickname)
        self.change_value_contact("title", contact.title)
        self.change_value_contact("company", contact.company)
        self.change_value_contact("address", contact.address)
        self.change_value_contact("home", contact.home)
        self.change_value_contact("mobile", contact.mobile)
        self.change_value_contact("work", contact.work)
        self.change_value_contact("fax", contact.fax)
        self.change_value_contact("email", contact.email)
        self.change_value_contact("email2", contact.email2)
        self.change_value_contact("email3", contact.email3)
        self.change_value_contact("homepage", contact.homepage)
        self.change_value_contact("bday", contact.bday)
        self.change_value_contact("bmonth", contact.bmonth)
        self.change_value_contact("byear", contact.byear)
        self.change_value_contact("aday", contact.aday)
        self.change_value_contact("amonth", contact.amonth)
        self.change_value_contact("ayear", contact.ayear)
        self.change_value_contact("address2", contact.address2)
        self.change_value_contact("notes", contact.notes)
        self.change_value_contact("phone2", contact.phone2)



    def change_value_contact(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="nav"]/ul/li[2]/a').click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def del_first_contact(self):
        wd = self.app.wd
        # переходим на домашнюю станицу
        self.open_home_page()
        wd.find_element_by_name('selected[]').click()
        wd.find_element_by_css_selector('[value="Delete"]').click()
        wd.switch_to_alert().accept()

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook") and len(wd.find_element_by_name('searchstring')) > 0):
            wd.find_element_by_link_text("home").click()

    def modification_first_contact(self, contact):
        wd = self.app.wd
        # переходим на домашнюю станицу
        self.open_home_page()
        # нажимаем кнопку изменить
        wd.find_element_by_css_selector('[title="Edit"]').click()
        # вносим изменения
        self.entering_personal_information(contact, wd)
        # нажимаем обновить
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def count_contacts(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name('selected[]'))


    def get_contact_list(self):
        wd = self.app.wd
        self.open_home_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            cells = element.find_elements_by_tag_name("td")
            firstname = cells[2]
            lastname = cells[1]
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(firstname=firstname.text, lastname=lastname.text, id=id))
        return contacts


