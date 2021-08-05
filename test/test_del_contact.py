

def test_delete_fist_contact(app):
    app.session.login(username="admin", password="secret")
    app.manager.del_first_contact()
    app.session.logout()