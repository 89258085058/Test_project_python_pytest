# -*- coding: utf-8 -*-
from model.group import Group


def test_modification_group(app):
    app.session.login( username="admin", password="secret")
    app.group.modification(Group(name="software", header="testing.", footer="ru"))
    app.session.logout()