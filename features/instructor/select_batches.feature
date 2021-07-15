Feature: Select Batches
  Scenario Outline: Instructor can successfully select a specific batch
    Given The User is logged in as an Instructor
    When The User clicks on a batch <batch_id>
    Then The title should say <title>
    Examples:
      | batch_id | title |
      | temp | Assessment Tracker - Batches by Week |
      | temp2 | Assessment Tracker - Batches by Week |