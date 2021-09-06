from model.contact import Contact
from model.group import Group
import random



def test_add_contact_to_group(app, orm, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_contact_list()) == 0:
        app.contact.add_personal_information(Contact(firstname="", lastname="", homephone="", mobilephone="",
                    workphone="", secondaryphone="", Address="", email="", email2="", email3=""))
    groups = orm.get_group_list()
    group = random.choice(groups)
    contacts = orm.get_contacts_not_in_group(Group(id=group.id))
    if not contacts:
        app.contact.add_personal_information(Contact(firstname="test", lastname="test", homephone="123", mobilephone="123",
                    workphone="123", secondaryphone="123", Address="123", email="123", email2="123", email3="123"))
        contacts = orm.get_contacts_not_in_group(Group(id=group.id))
    contact = random.choice(contacts)
    old_contacts_in_group = list(orm.get_contacts_in_group(Group(id=group.id)))
    app.contact.add_to_group_by_id(contact.id, group.name)
    new_contacts_in_group = list(orm.get_contacts_in_group(Group(id=group.id)))
    assert len(old_contacts_in_group) + 1 == len(new_contacts_in_group)
    assert contact in new_contacts_in_group


def test_delete_contact_from_group(app, orm, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_contact_list()) == 0:
        app.contact.add_personal_information(Contact(firstname="test", lastname="test", homephone="123", mobilephone="123",
                    workphone="123", secondaryphone="123", Address="123", email="123", email2="123", email3="123"))
    groups_with_contacts = orm.get_not_empty_group()
    if len(groups_with_contacts) == 0:
        rand_group = random.choice(orm.get_group_list())
        rand_contact = random.choice(orm.get_contact_list())
        app.contact.add_to_group_by_id(rand_contact.id, rand_group.name)
        groups_with_contacts = orm.get_not_empty_group()
    group = random.choice(groups_with_contacts)
    contacts = orm.get_contacts_in_group(group)
    contact = random.choice(contacts)
    app.contact.delete_from_group_by_id(contact.id, group.name)
    contact_in_group = list(orm.get_contacts_in_group(Group(id=group.id)))
    assert contact not in contact_in_group