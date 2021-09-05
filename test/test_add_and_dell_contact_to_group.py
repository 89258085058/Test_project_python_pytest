from fixture.orm import *
import random


def test_add_contact_to_group(app, orm):
    contact = None
    add_to_group = None
    all_groups = orm.get_group_list()
    if len(all_groups) == 0:
        app.group.add_personal_information(Contact(firstname="Alexandr", lastname="Gorelov"))
        all_groups = orm.get_group_list()
    for group in all_groups:
        contacts = orm.get_contacts_not_in_group(group)
        if len(contacts) > 0:
            contact = contacts[0]
            add_to_group = group
            break
    if contact is None:
        app.contact.add_personal_information(Contact(firstname="test", lastname="test"))
        contacts = sorted(orm.get_contact_list(), key=Contact.id_or_max)
        contact = contacts[len(contacts)-1]
    old_contacts = orm.get_contacts_in_group(add_to_group)
    app.contact.add_contact_to_group(contact, add_to_group)
    new_contacts = orm.get_contacts_in_group(add_to_group)
    assert len(old_contacts) + 1 == len(new_contacts) and new_contacts.count(contact) == 1


def test_del_random_contact_to_random_group(app, orm):
    contact = None
    add_to_group = None
    all_groups = orm.get_group_list()
    if len(all_groups) == 0:
        app.group.add_personal_information(Contact(firstname="Alexandr1", lastname="Gorelov1"))
        app.contact.add_contact_to_group(random.choice(orm.get_contact_list()), random.choice(orm.get_group_list()))
        all_groups = orm.get_group_list()
    for group in all_groups:
        contacts = orm.get_contacts_in_group(group)
        if len(contacts) > 0:
            contact = contacts[0]
            add_to_group = group
            break
    if contact is None and orm.get_contact_list() == 0:
        app.contact.add_personal_information(Contact(firstname="test1", lastname="test1"))
        contact = orm.get_contact_list()[0]
        add_to_group = random.choice(orm.get_group_list())
        app.contact.add_contact_to_group(contact, add_to_group)
    elif contact is None and orm.get_contact_list() != 0:
        contact = random.choice(orm.get_contact_list())
        add_to_group = random.choice(orm.get_group_list())
        app.contact.add_contact_to_group(contact, add_to_group)
    old_contacts = orm.get_contacts_in_group(add_to_group)
    app.contact.del_contact_to_group(contact, add_to_group)
    new_contacts = orm.get_contacts_in_group(add_to_group)
    assert len(old_contacts) - 1 == len(new_contacts) and new_contacts.count(contact) == 0
