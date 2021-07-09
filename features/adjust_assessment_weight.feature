Feature: Adjust assessment weight
  Scenario Outline: The Instructor successfully adjusts the weight of an assessment
    Given The User is logged in as an Instructor
    Given The Instructor is on a page for a <batch> batch
    When The Instructor clicks on a quiz
    Then The adjust-weight popup should be visible
    When The Instructor moves the dial to <num>
    When The Instructor clicks the save button
    Then The test-weight popup should disappear
    When The Instructor clicks on a quiz
    Then The adjust-weight popup should be visible
    Then The adjust-weight indicator should be <num>
    Examples:
      | batch | num |
      |Python | 50  |
      |Java   | 100 |
      |C++    | 75  |
      |C#     | 0   |