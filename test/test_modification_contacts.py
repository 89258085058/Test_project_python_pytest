# -*- coding: utf-8 -*-
from model.contact import Contact

def test_modification_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.manager.modification_first_contact(Contact(firstname="software", middlename="software", lastname="software", nickname="software", title="software", company="software",
                                                   address="software", home="00000", mobile="0000000", work="000000", fax="000000",
                                                   email="software@mail.ru", email2="software@yandex.ru", email3="software@gmail.ru", homepage="www.software.ru",
                                                   bday="5", bmonth="May", byear="1997", aday="10", amonth="January", ayear="2013", address2="software", notes="software software",
                                                   phone2="000000"))

    app.session.logout()
