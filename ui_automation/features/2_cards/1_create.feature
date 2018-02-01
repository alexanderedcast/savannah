# Created by nik-edcast at 12/18/17
Feature: Card creation
  """Verifying that possible to create all types of cart"""
  """
  1. Login
  2. Create a card
  3. Verify creation
  4. Delete a card
  """

  Scenario: Verify that possible to create simple Link SmartCard
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "SmartCard" with "Link" card
     And Verify that a card has been created
    Then "Delete" a card from your content

  Scenario: Verify that possible to create card simple from upload - Web Search
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "SmartCard" with "Upload" card
    And Verify that a card has been created
    Then "Delete" a card from your content

  Scenario: Verify that possible to create simple Text SmartCard
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "SmartCard" with "Text" card
    And Verify that a card has been created
    Then "Delete" a card from your content

  Scenario: Verify that possible to create simple Poll SmartCard
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "SmartCard" with "Poll" card
    And Verify that a card has been created
    Then "Delete" a card from your content

  Scenario: Verify that possible to create simple Quiz SmartCard
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "SmartCard" with "Quiz" card
    And Verify that a card has been created
    Then "Delete" a card from your content

  Scenario: Verify that possible to create card with a optional description
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Link" "SmartCard" with "description"
    And Verify that card has been created with "description"
    Then "Delete" a card from your content

  Scenario: Verify that possible to create a card with level of complexity for this card
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Link" "SmartCard" with "level of complexity"
    And Verify that card has been created with "level of complexity"
    Then "Delete" a card from your content

  Scenario: Verify that possible to create a card with tag
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Link" "SmartCard" with "tag"
    And Verify that card has been created with "tag"
    Then "Delete" a card from your content

  @BUG
  Scenario: Verify that possible to create the Poll card with link
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Poll" "SmartCard" with "link"
    And Verify that card has been created with "link"
    Then "Delete" a card from your content
 
  @BUG
  Scenario: Verify that possible to create card with content provider
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Link" "SmartCard" with "content provider"
    And Verify that card has been created with "content provider"
    Then "Delete" a card from your content

  Scenario: Verify that possible to create card with card type
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Link" "SmartCard" with "card type"
    And Verify that card has been created with "card type"
    Then "Delete" a card from your content

    #smartcard of smartcard







