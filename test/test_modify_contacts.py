# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_modify_contact_firstname_and_lastname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_personal_information(Contact(firstname="Alexandr", lastname="Gorelov"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_new = Contact(firstname="NEWAlexandr", lastname="NEWGorelov")
    contact_new.id = contact.id
    app.contact.modification_contact_by_id(contact.id, contact_new)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    index = 0
    for i in old_contacts:
        if i.id == contact.id:
            old_contacts[index] = contact_new
            break
        else:
            index = index + 1
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)