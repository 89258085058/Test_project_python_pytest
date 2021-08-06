# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="12345", header="12345", footer="12345"))



def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))







