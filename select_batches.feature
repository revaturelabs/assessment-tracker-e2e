Feature: Select Batches

#  Scenario Outline: Instructor logs into the application
#    Given The User is on the home page
#    When The User clicks on the login button
#    When The User enters <username> into the username field
#    # When The User enters <password> into the password field
#    Then The name displayed should say <name>
#    Examples:
#      | username | name |
#      | rs@revature.com | Ryan Schlientz |

  Scenario Outline: Instructor can successfully select a specific batch
    Given The User is logged in as an Instructor
    When The User clicks on a batch <batch_id>
    Then The title should say <title>
    Examples:
      | batch_id | title |
      | temp | Assessment Tracker - Batches by Week |