import re

def test_comparing_contact_home_page_db(app, db):
    All_id = db.get_all_contact_id()
    for id in All_id:
        contact_from_home_page = app.contact.get_contact_by_id(id)
        contact_from_db = db.get_contact_by_id(id)
        assert contact_from_home_page.firstname == contact_from_db.firstname
        assert contact_from_home_page.lastname == contact_from_db.lastname
        assert contact_from_home_page.Address == contact_from_db.Address
        assert contact_from_home_page.all_email_from_home_page == contact_from_db.all_email_from_home_page
        assert contact_from_home_page.all_phones_from_home_page == contact_from_db.all_phones_from_home_page


def clear(s):
    return re.sub("[() +-]", "", s)

def merge_phones_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone,
                                        contact.workphone, contact.phone2]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))