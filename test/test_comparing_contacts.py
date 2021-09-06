from fixture.db import *


def test_comparison_data_home_page_with_db(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.add_personal_information(Contact(firstname="Alexandr", lastname="Gorelov", id=id))
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_db = db.get_contact_list()
    assert sorted(contact_from_db, key=Contact.id_or_max) == sorted(contact_from_home_page, key=Contact.id_or_max)



