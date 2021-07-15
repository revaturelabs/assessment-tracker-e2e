Feature: See average grade
  Scenario Outline: Instructor can see an average grade for an assessment
    Given The User is logged in as an Instructor
    Given The Instructor is on a page for a <batch> batch
    Then The average grade is displayed on the batch page
    Examples:
      | batch |
      | Python|
      | Java  |