# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_firstname_and_lastname(app):
    old_cantacts = app.manager.get_contact_list()
    contact = Contact(firstname="test_name", lastname="test_lastname")
    contact.id = old_cantacts[0].id
    app.manager.add_personal_information(contact)
    new_contacts = app.manager.get_contact_list()
    assert len(old_cantacts) == len(new_contacts)
    old_cantacts[0] = contact
    assert sorted(old_cantacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_contact_middlename(app):
    #if app.manager.count_contacts() == 0:
        #app.manager.add_personal_information(Contact(middlename="test_midlename"))
    #app.manager.modification_first_contact(Contact(middlename="software"))