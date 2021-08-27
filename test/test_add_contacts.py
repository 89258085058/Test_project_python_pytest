# -*- coding: utf-8 -*-
from model.contact import Contact



def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_cantacts = app.contact.get_contact_list()
    app.contact.add_personal_information(contact)
    assert len(old_cantacts) + 1 == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_cantacts.append(contact)
    assert sorted(old_cantacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)










