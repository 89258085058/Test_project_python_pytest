from model.contact import Contact

def test_delete_fist_contact(app):
       app.manager.del_first_contact()
