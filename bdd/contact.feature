Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <first_name>, <last_name> and <address>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  | firstname | lastname |
  | Alex1     | gor1     |
  | Alex2     | gor2     |
  | Alex3     | gor3     |


Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without deleted contact


Scenario Outline: Modify a contact
  Given a non-empty contact list
  Given a random contact from the list
  Given a contact with <first_name>, <last_name> and <address>
  When I modify the contact from the list
  Then the new contact list is equal to the old list with modified contact

  Examples:
  | firstname | lastname |
  | TEST      | test1    |
  | TEST      | test2    |
  | TEST      | test3    |