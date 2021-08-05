# -*- coding: utf-8 -*-
from model.contact import Modification_contact

def test_modification_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.manager.modification_first_contact(Modification_contact(input_firstname="software", input_middlename="software", input_lastname="software", input_nickname="software", input_title="software", input_company="software",
                                                   input_address="software", input_home="00000", input_mobile="0000000", input_work="000000", input_fax="000000",
                                                   input_email="software@mail.ru", input_email2="software@yandex.ru", input_email3="software@gmail.ru", input_homepage="www.software.ru",
                                                   input_bday="5", input_bmonth="May", input_byear="1997", input_aday="10", input_amonth="January", input_ayear="2013", input_address2="software", input_notes="software software",
                                                   input_phone2="000000"))

    app.session.logout()
