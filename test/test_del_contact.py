from model.contact import Contact


def test_delete_fist_contact(app):
    if app.manager.count_contacts() == 0:
        app.manager.add_personal_information(Contact(firstname="test_name", middlename="test_middlename"))
    old_cantacts = app.manager.get_contact_list()
    app.manager.del_first_contact()
    new_contacts = app.manager.get_contact_list()
    assert len(old_cantacts) - 1 == len(new_contacts)
    old_cantacts[0:1] = []
    assert old_cantacts == new_contacts




