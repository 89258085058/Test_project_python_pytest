from model.contact import Contact
from random import randrange

def test_delete_some_contact(app):
    if app.manager.count_contacts() == 0:
        app.manager.add_personal_information(Contact(firstname="test_name", middlename="test_middlename"))
    old_cantacts = app.manager.get_contact_list()
    index = randrange(len(old_cantacts))
    app.manager.del_contact_by_index(index)
    new_contacts = app.manager.get_contact_list()
    assert len(old_cantacts) - 1 == len(new_contacts)
    old_cantacts[index:index+1] = []
    assert old_cantacts == new_contacts




