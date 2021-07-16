Feature: Admins can add new associates for adding to batches

    Scenario: An Admin succesfully adds a new associate
	Given The User is logged in as an Admin
	When  The User clicks the create associate button
	Then  The new associate popup should appear
	When  The User enters an email for the new associate
	When  The User enters a first name for the new associate
	When  The User enters a last name for the new associate
	When  The User selects the submit new associate button
	Then  The new associate popup should dissapear
	Then  The new User should appear in the list of associates

    Scenario: An Admin chooses not to add a new associate
	Given The User is logged in as an Admin
	When  The User clicks the create associate button
	Then  The new associate popup should appear
	When  The User enters an email for the new associate
	When  The User enters a first name for the new associate
	When  The User enters a last name for the new associate
	When  The User selects the cancel new associate button
	Then  The new associate popup should dissapear

    Scenario: An Admin enters invalid information for the new associate
	Given The User is logged in as an Admin
	When  The User clicks the create associate button
	Then  The new associate popup should appear
	When  The User enters a first name for the new associate
	When  The User enters a last name for the new associate
	When  The User selects the submit new associate button
	Then  A message should appear indicating the provided email is invalid
	When  The User selects the cancel new associate button
	Then  The new associate popup should dissapear