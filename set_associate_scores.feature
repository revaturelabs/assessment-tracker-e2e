Feature: Set Associate Scores
  Scenario Outline: Successfully updating a Score
    Given The User is logged in as an Instructor
    Given The Instructor is on a page for a specific <batch>
    When The Instructor clicks on an Associate <name> from a list
    When The Instructor sets a grade for an <assessment>
    When The Instructor clicks the <button> to save the Score
    Then A message should tell the Instructor that their grade was saved

    Examples:
      | batch | name |assessment|button|
      |Python - 20200120|Zachary|TEST| save1|
#     Week 1 assessment
      |iOS Development - 20210320|Kerry|iOS Quiz|save2|
#     Week 1 assessment
      |C++ - 20202222|Patrick|Cumulative|save3|
#     Week 1 assessment