from pytest_bdd import given, when, then
from model.contact import Contact
import random


#Create contact

@given('a contact list',
       target_fixture="contact_list")
def contact_list(db):
    return db.get_contact_list()


@given('a contact with <firstname>, <lastname>',
       target_fixture="new_contact")
def new_contact(firstname, lastname):
    return Contact(firstname=firstname, lastname=lastname)


@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.add_personal_information(new_contact)


@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(db, contact_list, new_contact):
    old_contacts_lst = contact_list
    new_contacts_lst = db.get_contact_list()
    old_contacts_lst.append(new_contact)
    assert sorted(old_contacts_lst, key=Contact.id_or_max) == sorted(new_contacts_lst, key=Contact.id_or_max)

#------------------------------------------------------------------------------------------------------------
#Delete contact

@given('a non-empty contact list', target_fixture="non_empty_contact_list")
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.add_personal_information(Contact(firstname="name"))
    return db.get_contact_list()

@given('a random contact from the list', target_fixture="random_contact")
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@when('I delete the contact from the list')
def delete_group(app, random_contact):
    app.contact.del_contact_by_id(random_contact.id)

@then('the new contact list is equal to the old list without the deleted group')
def verify_group_deleted(db, non_empty_contact_list, app, check_ui):
    old_cantacts = non_empty_contact_list
    contact = random.choice(old_cantacts)
    app.contact.del_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    old_cantacts.remove(contact)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)



#------------------------------------------------------------------------------------------------------------
#Modify contact

@given('a non-empty contact list', target_fixture='non_empty_contact_list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.add_personal_information(Contact(firstname="Alexandr", lastname="Gorelov"))
    return db.get_contact_list()


@when('I modify the contact')
def modify_contact(app, db):
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_new = Contact(firstname="NEWAlexandr", lastname="NEWGorelov")
    contact_new.id = contact.id
    app.contact.modification_contact_by_id(contact.id, contact_new)


@then('the new contact list is equal to the old list with the modified contact')
def verify_contact_modified(app, db, non_empty_contact_list, check_ui):
    old_contacts = non_empty_contact_list
    contact = random.choice(old_contacts)
    contact_new = Contact(firstname="NEWAlexandr", lastname="NEWGorelov")
    contact_new.id = contact.id
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    index = 0
    for i in old_contacts:
        if i.id == contact.id:
            old_contacts[index] = contact_new
            break
        else:
            index = index + 1
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
