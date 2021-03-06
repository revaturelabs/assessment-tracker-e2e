Feature: Add Notes
  Scenario Outline: Instructor can successfully make a note for an associate for a given week
    Given The User is logged in as an instructor
    Given The Instructor is on a page for a <batch> batch
    When The Instructor selects week number <number>
    When The Instructor clicks on an associate's name
    Then A popup appears where the Instructor can add or edit a note
    Then The Instructor adds their note
    Then The Instructor clicks Create
    Then The new note is saved
    Examples:
      | batch | number |
      | Java  | 1      |
      | Python| 2      |