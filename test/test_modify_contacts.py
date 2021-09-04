# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_modify_contact_firstname_and_lastname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_personal_information(Contact(firstname="1", lastname="1", homephone="1", mobilephone="1",
                                                     workphone="1", secondaryphone="1", Address="1", email="1", email2="1", email3="1"))
    old_cantacts = db.get_contact_list()
    contact = random.choice(old_cantacts)
    app.contact.modification_contact_by_id(contact.id, Contact(firstname="5", lastname="5", homephone="5", mobilephone="5",
                   workphone="5", secondaryphone="5", Address="5", email="5", email2="5", email3="5"))
    new_contacts = db.get_contact_list()
    assert len(old_cantacts) == len(new_contacts)
    old_cantacts = db.get_contact_list()
    assert old_cantacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                      key=Contact.id_or_max)

