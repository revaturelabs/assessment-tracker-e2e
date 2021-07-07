Feature: Add Assessment
  Scenario: Instructor can successfully add an assessment
    Given The User is logged in as an Instructor
    Given The Instructor is on a page for a Batch
    When The Instructor clicks on a Plus Assessment Button
    When The Instructor selects an Assessment Type
    When The Instructor enters a name for the Assessment
    When The Instructor clicks the button to create the Assessment
    Then The list of Assessments for that week is updated with the new one