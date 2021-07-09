Feature: Set Associate Scores
  Scenario Outline: Successfully updating a Score
    Given The User is logged in as an Instructor
    Given The Instructor is on a page for a <batch> batch
    When The Instructor clicks on an Associate <name> from a list
    When The Instructor sets a grade for an <assessment>
    When The Instructor clicks the <button> to save the Score
    Then A message should tell the Instructor that their grade was saved

    Examples:
      | batch | name |assessment|button|
      |Python|Zachary|TEST| save1|
#     Week 1 assessment
      |iOS Development|Kerry|iOS Quiz|save2|
#     Week 1 assessment
      |C++|Patrick|Cumulative|save3|
#     Week 1 assessment