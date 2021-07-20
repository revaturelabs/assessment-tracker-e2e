Feature: View averages across categories
  Scenario: Admin views averages
    Given The User is logged in as an Admin
    When The admin clicks the Assessments button
    Then  The admin should be navigated to a page displaying averages of all assessments across Revature