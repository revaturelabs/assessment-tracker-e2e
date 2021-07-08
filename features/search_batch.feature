Feature: Users can search for a specific batch

  Scenario Outline: Search from the Search Bar
    Given The User is logged in as an Instructor
    When The Instructor types <Name> into the Search Bar
    Then A list of results is displayed beneath the Search Bar
    When The Instructor clicks on a result
    Then They are taken to the page for that Batch

    Examples:
      | Name |
      | Python |
      | Java |
      | C# |