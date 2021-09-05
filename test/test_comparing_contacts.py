from model.contact import Contact


def test_check_all_contact(app, db):
    # информация с главной страницы контактов
    all_contact_main_page = app.contact.get_contact_list()
    # информация из базы данных
    all_contact_db = db.get_contact_list()
    # Сравниваем список контактов
    assert sorted(all_contact_main_page, key=Contact.id_or_max) == sorted(all_contact_db, key=Contact.id_or_max)
    #print(all_contact_main_page)
    #print(all_contact_db)