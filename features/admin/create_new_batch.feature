Feature: Admins can create new batches
  Scenario: Admin can create a valid batch from existing associates
    Given The User is logged in as an Admin
    When  The User enters a batch name in the batch name input
    When  The User enters a track name in the track name input
    When  The User enters an end date in the end date input
    When  The User selects five associates to be added to the new batch
    Then  The five selected associates should appear in the added associates list
    When  The submit create new batch button is pressed
    Then  A batch created popup should appear

  Scenario: Admin can create a valid batch from specific associates
    Given The User is logged in as an Admin
    When  The User enters a batch name in the batch name input
    When  The User enters a track name in the track name input
    When  The User enters an end date in the end date input
    When  The User enters ba into the search input
    Then  All associates in the associate list should start with ba
    When  The User selects the associates in the associate list
    Then  The selected associates should appear in the added associates list
    When  The submit create new batch button is pressed
    Then  A batch created popup should appear