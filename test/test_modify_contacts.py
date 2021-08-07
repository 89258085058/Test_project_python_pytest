# -*- coding: utf-8 -*-
from model.contact import Contact

def test_modify_contact_firstname_and_lastname(app):
     app.manager.modification_first_contact(Contact(firstname="software", lastname="software"))


def test_modify_contact_middlename(app):
    app.manager.modification_first_contact(Contact(middlename="software"))