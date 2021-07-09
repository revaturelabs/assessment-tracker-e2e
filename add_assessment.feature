Feature: Add Assessment
 Scenario Outline: Instructor can successfully add an assessment
    Given The User is logged in as an Instructor
    Given The Instructor is on a page for a <batch> batch
    When The Instructor clicks on a Plus Assessment Button
    When The Instructor selects the assessment type <assessment_type>
    When The Instructor enters a name of <name> for the Assessment
    When The Instructor clicks the button to create the Assessment
    Then The list of Assessments for that week is updated with the new one (<name>)
    Examples:
      | batch         | assessment_type | name          |
      |Python         |QC               |Python Selenium|
      |Java           |Quiz             |Java Selenium  |
      |C++            |One-on-Ones      |The Selenium   |
      |C#             |Project          |El Selenium    |
      |iOS Development|QC               |iOS Selenium   |

