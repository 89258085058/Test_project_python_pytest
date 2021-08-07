# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.manager.add_personal_information(Contact(firstname="alexandr", middlename="sergeevich", lastname="gorelov", nickname="asgorelov", title="12345", company="bolid",
                                      address="zelenograd", home="89555555", mobile="89258085058", work="89000000000", fax="87000000000",
                                      email="asgorelov@mail.ru", email2="asgorelov@yandex.ru", email3="asgorelov@gmail.ru", homepage="www.134423.ru",
                                      address2="zelenograd", notes="privet info",
                                      phone2="12345"))






def test_add_empty_contact(app):
    app.manager.add_personal_information(Contact( firstname="", middlename="", lastname="", nickname="", title="", company="",
                                      address="", home="", mobile="", work="", fax="",
                                      email="", email2="", email3="", homepage="",
                                      address2="", notes="",
                                      phone2=""))
   