from model.contact import Contact
import  re

class ContactHelper:

    def __init__(self, app):
        self.app = app


    def add_personal_information(self, contact):
        wd = self.app.wd
        self.add_new_contact()
        self.entering_personal_information(contact)
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()
        self.contact_cache = None

    def entering_personal_information(self, contact):
        self.change_value_contact("firstname", contact.firstname)
        self.change_value_contact("lastname", contact.lastname)
        self.change_value_contact("home", contact.homephone)
        self.change_value_contact("mobile", contact.mobilephone)
        self.change_value_contact("work", contact.workphone)
        self.change_value_contact("phone2", contact.secondaryphone)
        self.change_value_contact("address", contact.Address)
        self.change_value_contact("email", contact.email)
        self.change_value_contact("email2", contact.email2)
        self.change_value_contact("email3", contact.email3)



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
        self.del_contact_by_index(0)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name('selected[]').click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name('selected[]')[index].click()

    def del_contact_by_index(self, index):
        wd = self.app.wd
        # переходим на домашнюю станицу
        self.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_css_selector('[value="Delete"]').click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook") and len(wd.find_element_by_name('searchstring')) > 0):
            wd.find_element_by_link_text("home").click()

    def select_edit_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_css_selector('[title="Edit"]')[index].click()

    def modification_first_contact(self):
        wd = self.app.wd
        self.modification_contact_by_index(0)


    def modification_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_home_page()
        self.select_edit_contact_by_index(index)
        self.entering_personal_information(contact, wd)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def count_contacts(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name('selected[]'))

    contact_cache = None


    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                Address = cells[3].text
                all_email = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  all_phones_from_home_page=all_phones, Address=Address,
                                                  all_email_from_home_page=all_email))

        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        Address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone, Address=Address, email=email, email2=email2, email3=email3)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name('a').click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name('a').click()

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        findallname= re.search("(.*)", text).group(1)
        addsub = re.sub((" "), ("\n"), findallname)
        firstname = re.search("(.*)", addsub).group(1)
        lastname = re.search("(.*)\n(.*)", addsub).group(2)
        Address = re.search("(.*)\n(.*)", text).group(2)
        email = wd.find_element_by_xpath('//*[@id="content"]/a[1]').text
        email2 = wd.find_element_by_xpath('//*[@id="content"]/a[2]').text
        email3 = wd.find_element_by_xpath('//*[@id="content"]/a[3]').text
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone,
                       Address=Address, firstname=firstname, lastname=lastname,
                       email=email, email2=email2, email3=email3)


