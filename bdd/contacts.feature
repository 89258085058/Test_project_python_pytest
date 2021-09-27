Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <lastname>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
| firstname  |  lastname  |
| Alex1      | Gor1       |
| Alex12     | Gor2       |


Scenario Outline: Modify contact
  Given a non-empty contact list
  Given a random contact from the list
  When I modify the contact
  Then the new contact list is equal to the old list with the modified contact



Scenario: Delete a contact
    Given a non-empty contact list
    Given a random contact from the list
    When I delete the contact from the list
    Then the new contact list is equal to the old list without the deleted group