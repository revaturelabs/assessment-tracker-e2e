Feature: Adjust assessment weight
  Scenario Outline: The Instructor successfully adjusts the weight of an assessment
    Given The User is logged in as an Instructor
    Given The Instructor is on a page for a Batch
    When The Instructor clicks on a quiz
    Then The test-weight popup should be visible
    When The Instructor moves the dial to <num>
    When The Instructor clicks the save button
    Then The test-weight popup should disappear
    When The Instructor clicks on a quiz
    Then The test-weight popup should be visible
    Then The the test-weight indicator should be <num>
    Examples:
      | num |
      |  50 |
      |  100|
      |  75 |
      |  0  |