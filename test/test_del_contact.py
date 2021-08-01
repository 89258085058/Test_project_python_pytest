
def test_delete_contact(app):
    app.session.login(username="admin", password="secret")
    app.manager.del_contact()
    app.session.logout()