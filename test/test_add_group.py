# -*- coding: utf-8 -*-
from model.group import Group
from fixture.aplication import Aplication
import pytest



@pytest.fixture
def app(request):
    fixture = Aplication()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login( username="admin", password="secret")
    app.create_group( Group(name="12345", header="12345", footer="12345"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()



