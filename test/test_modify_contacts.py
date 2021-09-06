# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_modify_contact_firstname_and_lastname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_personal_information(Contact(firstname="Alexandr", lastname="Gorelov"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    index = old_contacts.index(contact)
    new_contact = (Contact(firstname="TestName", lastname="TestLastName"))
    app.contact.modification_contact_by_id(contact.id, new_contact)
    assert len(old_contacts) == app.contact.count_contacts()
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
