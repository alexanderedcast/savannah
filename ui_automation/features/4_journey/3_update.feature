# Created by nik-edcast at 12/21/17
Feature: Update Journey
"""This scenario verify , that it is possible to update the Pathway"""
  """
  1. Login
  2. Create a Journey
  3. Edit a Journey
  4. Verify editing
  5. Delete a Journey
  """
  @BUG
  Scenario: Verify that possible to edit Journey by adding card
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Journey" with "Link" card
    And Verify that a card has been created
    Then Verify Edit option for "Link" Journey
    Then "Delete" a card from your content

  @BUG
  Scenario: Verify that possible to edit created - delete all cards from Pathway
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Journey" with "Upload" card
    And Verify that a card has been created
    Then Edit "Journey": "delete card from journey"
    Then "Delete" a card from your content

  @BUG
  Scenario: Verify that possible to edit created Journey and update title
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Journey" with "Link" card
    And Verify that a card has been created
    Then Edit "Journey": "edit title"
    Then "Delete" a card from your content

  @BUG
  Scenario: Verify that possible to edit created Journey and update description
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Journey" with any card and "description"
    And Verify that a card has been created
    Then Edit "Journey": "edit description"
    Then "Delete" a card from your content

  @BUG
  Scenario: Verify that possible to edit created Journey and update channel
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Journey" with any card and "post to channel"
    And Verify that a card has been created
    Then Edit "Journey": "edit channel"
    Then "Delete" a card from your content

 @BUG
 Scenario: Verify that possible to edit created Journey and update level of complexity
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Journey" with any card and "level of complexity"
    And Verify that a card has been created
    Then Edit "Journey": "edit level of complexity"
    Then "Delete" a card from your content