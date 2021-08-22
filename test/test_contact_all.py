import re
from random import randrange
from model.contact import Contact


def test_all_contct_on_home_page(app):
    if app.contact.count_contacts() == 0:
        app.contact.add_personal_information(Contact(firstname="Alexandr", lastname="Gorelov", id=id,
                       homephone="999", mobilephone="888",
                       workphone="777", secondaryphone="666", Address="Moscow", email="123@mail.ru", email2="12345@mail.ru", email3="123456@mail.ru"))
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.Address == contact_from_edit_page.Address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)


def test_all_contact_on_contact_view_page(app):
    if app.contact.count_contacts() == 0:
        app.contact.add_personal_information(Contact(firstname="Alexandr", lastname="Gorelov", id=id,
                                                     homephone="999", mobilephone="888",
                                                     workphone="777", secondaryphone="666", Address="Moscow",
                                                     email="123@mail.ru", email2="12345@mail.ru",
                                                     email3="123456@mail.ru"))
    old_cantacts = app.contact.get_contact_list()
    index = randrange(len(old_cantacts))
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.firstname == contact_from_edit_page.firstname
    assert contact_from_view_page.lastname == contact_from_edit_page.lastname
    assert contact_from_view_page.Address == contact_from_edit_page.Address
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone
    assert contact_from_view_page.email == contact_from_edit_page.email
    assert contact_from_view_page.email2 == contact_from_edit_page.email2
    assert contact_from_view_page.email3 == contact_from_edit_page.email3



def clear(s):
    return re.sub("[() -]","", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.email, contact.email2, contact.email3]))))