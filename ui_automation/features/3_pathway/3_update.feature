# Created by nik-edcast at 12/21/17
Feature: Update Pathway
"""This scenario verify , that it is possible to update the Pathway"""
  """
  1. Login
  2. Create a Pathway
  3. Edit a Pathway
  4. Verify editing
  5. Delete a Pathway
  """
  Scenario: Verify that possible to edit Pathway by adding card
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with "Link" card
    And Verify that a card has been created
    Then Verify Edit option for "Link" Pathway
    Then "Delete" a card from your content

  Scenario: Verify that possible to edit created - delete all cards from Pathway
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with "Upload" card
    And Verify that a card has been created
    Then Edit "Pathway": "delete card from pathway"
    Then "Delete" a card from your content

  Scenario: Verify that possible to edit created Pathway and update title
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with "Link" card
    And Verify that a card has been created
    Then Edit "Pathway": "edit title"
    Then "Delete" a card from your content

  Scenario: Verify that possible to edit created Pathway and update description
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with any card and "description"
    And Verify that a card has been created
    Then Edit "Pathway": "edit description"
    Then "Delete" a card from your content

  Scenario: Verify that possible to edit created Pathway and update channel
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with any card and "post to channel"
    And Verify that a card has been created
    Then Edit "Pathway": "edit channel"
    Then "Delete" a card from your content

 Scenario: Verify that possible to edit created Pathway and update level of complexity
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with any card and "level of complexity"
    And Verify that a card has been created
    Then Edit "Pathway": "edit level of complexity"
    Then "Delete" a card from your content