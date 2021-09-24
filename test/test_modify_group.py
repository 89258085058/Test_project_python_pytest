from model.group import Group
import random
import allure


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="testName", header="testHeader", footer="testFooter"))
    with allure.step('Given a non-empty group list'):
        old_groups = db.get_group_list()
    with allure.step('Given a random group from the list'):
        group = random.choice(old_groups)
    with allure.step('When I modify the group bu id'):
        app.group.modify_group_by_id(group.id, Group(name="New", header="New", footer="New"))
    with allure.step('Then the new group list is equal to the old list with modified group'):
        new_groups = db.get_group_list()
        assert len(old_groups) == len(new_groups)
        old_groups = db.get_group_list()
        assert old_groups == new_groups
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

