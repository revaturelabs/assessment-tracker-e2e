Feature: Set Associate Scores
  Scenario Outline: Successfully updating a Score
    Given The User is logged in as an Instructor
    Given The Instructor is on a page for a <batch> batch
    When The Instructor clicks on an Associate <name> for the <assessment> assessment
    When The Instructor clicks the save score button 
    Then A message should tell the Instructor that their grade was saved

    Examples:
      | batch | name |assessment|
      |Python|Zachary|TEST|
#     Week 1 assessment
      |iOS Development|Kerry|bbbb|
      # |iOS Development|Kerry|iOS Quiz|
#     Week 1 assessment
      |C++|Patrick|The Selenium|
      # |C++|Patrick|Cumulative|
#     Week 1 assessment