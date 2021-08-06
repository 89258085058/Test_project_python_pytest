# -*- coding: utf-8 -*-
from model.contact import Contact

def test_modify_contact_firstname_and_lastname(app):
    if app.manager.count_contacts() == 0:
        app.manager.add_personal_information(Contact(firstname="test_name", lastname="test_lastname"))
    app.manager.modification_first_contact(Contact(firstname="software", lastname="software"))


def test_modify_contact_middlename(app):
    if app.manager.count_contacts() == 0:
        app.manager.add_personal_information(Contact(middlename="test_midlename"))
    app.manager.modification_first_contact(Contact(middlename="software"))