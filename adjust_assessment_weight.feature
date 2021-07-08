Feature: Adjust assessment weight
  Scenario: The Instructor successfully adjusts the weight of an assessment
    Given The User is logged in as an Instructor
    Given The Instructor is on a page for a Batch
    When The Instructor clicks on a quiz
    Then The adjust-weight popup should be visible
    When The Instructor moves the dial to 50
    When The Instructor clicks the save button
    Then The test-weight popup should disappear
    When The Instructor clicks on a quiz
    Then The adjust-weight popup should be visible
    Then The adjust-weight indicator should be 50
#    Examples:
#      | num |
#      |  50 |
#      |  100|
#      |  75 |
#      |  0  |