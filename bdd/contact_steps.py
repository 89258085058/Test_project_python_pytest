from pytest_bdd import given, when, then
from model.contact import Contact
import random


@given('a contact list')
def contact_list(db):
    return db.get_contact_list()


@given('a contact with <first_name>, <last_name> and <address>')
def new_contact(firstname, lastname):
    return Contact(firstname=firstname, lastname=lastname)


@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.add_personal_information(new_contact)


@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@given('a non-empty contact list')
def non_empty_contact_list(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.add_personal_information(Contact(firstname="TEST contact"))
    return db.get_contact_list()


@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.del_contact_by_id(random_contact.id)


@then('the new contact list is equal to the old list without deleted contact')
def verify_contact_deleted(db, non_empty_contact_list, random_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert \
            sorted(
                map(lambda x: Contact(
                    id=x.id,
                    firstname=x.firstname.strip(),
                    lastname=x.lastname.strip()
                ), new_contacts), key=Contact.id_or_max
            ) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


@when('I modify the contact from the list')
def modify_contact(app, new_contact, random_contact):
    new_contact.id = random_contact.id
    app.contact.modification_contact_by_id(random_contact.id, new_contact)


@then('the new contact list is equal to the old list with modified contact')
def verify_contact_modified(db, non_empty_contact_list, new_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    [x for x in old_contacts if x.id == new_contact.id][0].first_name = new_contact.first_name
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert \
            sorted(
                map(lambda x: Contact(
                    id=x.id,
                    firstname=x.firstname.strip(),
                    lastname=x.lastname.strip(),
              ), new_contacts), key=Contact.id_or_max
            ) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)