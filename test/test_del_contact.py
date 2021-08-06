from model.contact import Contact

def test_delete_fist_contact(app):
    if app.manager.count_contacts() == 0:
        app.manager.add_personal_information(Contact(firstname="test_name", middlename="test_middlename", lastname="last_name_test"))
    app.manager.del_first_contact()
