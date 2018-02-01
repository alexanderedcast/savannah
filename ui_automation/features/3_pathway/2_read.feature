# Created by nik-edcast at 12/18/17
Feature: Read a Pathway
  """Verifying that possible to read all types of cart"""
  """
  1. Login
  2. Create a card
  3. Verify creation
  4. Read a card
  5. Delete a card
  """
  Scenario: Verify that possible to read created Link Pathway
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with "Link" card
    And Verify that a card has been created
    Then Check if you can read the "Pathway" with "Link" card
    Then "Delete" a card from your content

  Scenario: Verify that possible to read created Upload Pathway
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with "Upload" card
    And Verify that a card has been created
    Then Check if you can read the "Pathway" with "Upload" card
    Then "Delete" a card from your content

  Scenario: Verify that possible to read created Poll Pathway
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with "Poll" card
    And Verify that a card has been created
    Then Check if you can read the "Pathway" with "Poll" card
    Then "Delete" a card from your content

  Scenario: Verify that possible to read created Quiz Pathway
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with "Quiz" card
    And Verify that a card has been created
    Then Check if you can read the "Pathway" with "Quiz" card
    Then "Delete" a card from your content

  # no ECL content > test fail
   @BUG
  Scenario: Verify that possible to read created Dynamic Pathway Pathway
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with "Dynamic Pathway" card
    And Verify that a card has been created
    Then Check if you can read the "Pathway" with "Dynamic Pathway" card
    Then "Delete" a card from your content

  """
  As Like I have in my Expertise I have Python
  And I will bookmark card from Discover
  """
   # no ECL content > test fail
   @BUG
  Scenario: Verify that possible to read created From Bookmark Pathway
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigating to "DISCOVER" page
    And Pick some card and "Bookmark" and store title of this card
    Then Create "Pathway" with "From Bookmark" card
    And Verify that a card has been created
    Then Check if you can read the "Pathway" with "From Bookmark" card
    Then "Delete" a card from your content

   # no ECL content > test fail
  @BUG
  Scenario: Verify that possible to read created Search SmartCard Pathway
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with "Search SmartCard" card
    And Verify that a card has been created
    Then Check if you can read the "Pathway" with "Search SmartCard" card
    Then "Delete" a card from your content

  Scenario: Verify that possible to read created Text Pathway
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with "Text" card
    And Verify that a card has been created
    Then Check if you can read the "Pathway" with "Text" card
    Then "Delete" a card from your content
