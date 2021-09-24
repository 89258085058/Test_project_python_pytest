# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import allure


def test_modify_contact_firstname_and_lastname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_personal_information(Contact(firstname="Alexandr", lastname="Gorelov"))
    with allure.step('Given a non-empty contact list'):
        old_contacts = db.get_contact_list()
    with allure.step('Given a random contact from the list'):
        contact = random.choice(old_contacts)
    with allure.step('Given a contact with first_name and last_name'):
        contact_new = Contact(firstname="NEWAlexandr", lastname="NEWGorelov")
    contact_new.id = contact.id
    with allure.step('When I modify the contact from the list'):
        app.contact.modification_contact_by_id(contact.id, contact_new)
    with allure.step('Then the new contact list is equal to the old list with modified contact'):
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