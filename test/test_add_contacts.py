# -*- coding: utf-8 -*-
from model.contact import Contact
import allure


def test_add_contact(app, db, check_ui, json_contacts):
    contact = json_contacts
    with allure.step('Given a contact list'):
        old_cantacts = db.get_contact_list()
    with allure.step('When I add the contact to the list'):
        app.contact.add_personal_information(contact)
    with allure.step('Then the new contact list is equal to the old list with the added contact'):
        assert len(old_cantacts) + 1 == app.contact.count_contacts()
        new_contacts = db.get_contact_list()
        old_cantacts.append(contact)
        assert old_cantacts == new_contacts
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.address.get_address_list(), key=Contact.id_or_max)
