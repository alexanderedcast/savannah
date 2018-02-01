# Created by nik-edcast at 12/18/17
Feature: Update a SmartCard
  """Verifying that possible to read all types of cart"""
  """
  1. Login
  2. Create a card
  3. Verify creation
  4. Update a card
  5. Verify a update option
  5. Delete a card
  """


  """https://jira.edcastcloud.com/browse/EP-8980"""
  @BUG
  Scenario: Verify that possible to update Link SmartCard
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    When Create "SmartCard" with "Link" card
    And Verify that a card has been created
    Then Verify that possible to "Edit" a "Link" SmartCard
    And Verify the edit option for "Link" SmartCard
    And "Delete" a card from your content

  Scenario: Verify that possible to update card from upload - Web Search
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    When Create "SmartCard" with "Upload" card
    And Verify that a card has been created
    Then Verify that possible to "Edit" a "Upload" SmartCard
    And Verify the edit option for "Upload" SmartCard
    And "Delete" a card from your content

  """
  text from input field don't erase
  """
  @BUG
  Scenario: Verify that possible to update Text SmartCard
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    When Create "SmartCard" with "Text" card
    And Verify that a card has been created
    Then Verify that possible to "Edit" a "Text" SmartCard
    Then Verify the edit option for "Text" SmartCard
    And "Delete" a card from your content

  Scenario: Verify that possible to update Poll SmartCard
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    When Create "SmartCard" with "Poll" card
    And Verify that a card has been created
    Then Verify that possible to "Edit" a "Poll" SmartCard
    And Verify the edit option for "Poll" SmartCard
    Then "Delete" a card from your content

  """https://jira.edcastcloud.com/browse/EP-9153"""
  @BUG
   Scenario: Verify that possible to create the Poll card with link
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Poll" "SmartCard" with "picture"
    And Verify that a card has been created
    And Verify the edit option for "Poll with picture" SmartCard change picture with Link
    Then Verify that possible to read "Poll with video" SmartCard
    Then "Delete" a card from your content




