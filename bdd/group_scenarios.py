from pytest_bdd import scenario
from .group_steps import *

@scenario('groups.feature', 'add new group')
def test_add_new_group():
    pass


@scenario('groups.feature', 'Delete a group')
def test_delete_group():
    pass