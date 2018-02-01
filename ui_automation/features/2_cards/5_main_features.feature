# Created by nik-edcast at 12/18/17
Feature: Actions with card

"""Verify that user can perform actions with card"""
  """
  1. Login
  2. Create card
  3. Perform action
  4. Verify this action
  5. Delete card
  """
  Scenario: Verify user has access to manage content -- "Add to Pathway"
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    And Create "Pathway" with "Text" card
    When Create "SmartCard" with "Text" card
    And Verify that a card has been created
    Then "Add to Pathway" the card

  Scenario: Verify user has access to manage content -- "Delete" content out of pathway
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    And Navigate to "ME" page "Content" tab
    Then Find and "Edit" Pathway and delete added card from Pathway
    And "Delete" all created data

  Scenario: Verify user has access to manage content -- "Post to Channel"
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    When Create "SmartCard" with "Text" card
    And "Post to Channel" a card and then verify in a "PUBLIC-NIK" channel
    Then Navigating to "DISCOVER" page
    And Verify in "PUBLIC-NIK" channel
    And Verify that a card has been created and posted to the channel

  Scenario: Verify user has access to manage content -- "Delete posted card" from channel
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigating to "DISCOVER" page
    And Verify in "PUBLIC-NIK" channel
    Then "Delete" a card from a channel

  Scenario: Verify that user able to use option Assign to Me card
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    When Create "SmartCard" with "Text" card
    Then "Assign to Me" a piece of content
    And Verify "Assign to Me" option
    Then "Delete" a card

  Scenario: Verify user has access to manage content -- "Promote" a piece of new content and see it in "Featured"
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    When Create "SmartCard" with "Text" card
    Then Verify "Promote" card feature
    And Navigate to "HOME" page "FEATURED" tab
    And Verify that a card has been promoted

 Scenario: Verify user has access to manage content -- "Unpromote" a piece of new content and see it in "Featured"
    Given Sign in as "existing user"
    And Navigate to "HOME" page "FEATURED" tab
    Then Verify "Unpromote" card feature
    And Navigate to "ME" page "Content" tab
    Then "Delete" a card

  Scenario: Verify that user able to complete SmartCard using Mark As Complete from dropdown menu
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    When Create "SmartCard" with "Text" card
    Then Verify that possible to "Mark as Complete" a SmartCard
    Then "Delete" a card



