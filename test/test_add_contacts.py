# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", homephone="", mobilephone="",
                    workphone="", secondaryphone="", Address="", email="", email2="", email3="")] +[
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10), homephone=random_string("homephone", 10), mobilephone=random_string("mobilephone", 10),
                workphone=random_string("workphone", 10), secondaryphone=random_string("secondaryphone", 10), Address=random_string("Address", 10),
                email=random_string("email", 10), email2=random_string("email2", 10), email3=random_string("email3", 10))
    for i in range(5)
    ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_cantacts = app.contact.get_contact_list()
    app.contact.add_personal_information(contact)
    assert len(old_cantacts) + 1 == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_cantacts.append(contact)
    assert sorted(old_cantacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)










