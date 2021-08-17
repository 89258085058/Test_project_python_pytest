# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_cantacts = app.manager.get_contact_list()
    contact = Contact(firstname="alexandr", middlename="sergeevich", lastname="gorelov", nickname="", title="", company="",
                                      address="", home="", mobile="", work="", fax="",
                                      email="", email2="", email3="", homepage="",
                                      address2="", notes="",
                                      phone2="")
    app.manager.add_personal_information(contact)
    assert len(old_cantacts) + 1 == app.manager.count_contacts()
    new_contacts = app.manager.get_contact_list()
    old_cantacts.append(contact)
    assert sorted(old_cantacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_empty_contact(app):
    #old_cantacts = app.manager.get_contact_list()
    #contact = Contact( firstname="", middlename="", lastname="", nickname="", title="", company="",
                                      #address="", home="", mobile="", work="", fax="",
                                      #email="", email2="", email3="", homepage="",
                                      #address2="", notes="",
                                      #phone2="")
    #app.manager.add_personal_information(contact)
    #new_contacts = app.manager.get_contact_list()
    #assert len(old_cantacts) + 1 == len(new_contacts)
    #old_cantacts.append(contact)
    #assert sorted(old_cantacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)