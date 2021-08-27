from model.contact import Contact
from random import randrange

def test_delete_some_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.add_personal_information(Contact(firstname="", lastname="", homephone="", mobilephone="",
                    workphone="", secondaryphone="", Address="", email="", email2="", email3=""))
    old_cantacts = app.contact.get_contact_list()
    index = randrange(len(old_cantacts))
    app.contact.del_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_cantacts) - 1 == len(new_contacts)
    old_cantacts[index:index+1] = []
    assert old_cantacts == new_contacts




