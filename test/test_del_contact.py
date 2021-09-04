import random
from model.contact import Contact


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_personal_information(Contact(firstname="", lastname="", homephone="", mobilephone="",
                    workphone="", secondaryphone="", Address="", email="", email2="", email3=""))
    old_cantacts = db.get_contact_list()
    contact = random.choice(old_cantacts)
    app.contact.del_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    old_cantacts.remove(contact)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
