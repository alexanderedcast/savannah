# Created by nik-edcast at 1/25/18
Feature: Main features with Pathway

  Scenario: Verify post like feature Pathway
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with "Text" card
    And Verify that a card has been created
    Then Leave a "like" on the card and verify the "post" action

  Scenario: Verify remove like feature Pathway on Me - Content
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    And Navigate to "ME" page "Content" tab
    Then Leave a "like" on the card and verify the "remove" action
    And "Delete" a card from your content

  Scenario: Verify leave comment feature for Pathway
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with "Text" card
    And Verify that a card has been created
    Then "Leave" a comment for "Pathway"

  Scenario: Verify delete comment feature Pathway
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    And Navigate to "ME" page "Content" tab
    Then "Delete" a comment for "Pathway"
    And "Delete" a card from your content

  """Create a method if I have more than one card inside a pathway"""
  """https://jira.edcastcloud.com/browse/EP-9977"""
  """
  In order to complete a Pathway you have to complete cards inside Pathway
  """
  @BUG
  Scenario: Verify mark as complete feature
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with "Text" card
    And Verify that a card has been created
    Then Verify that possible to completed "Pathway"
    And "Delete" a card from your content

  Scenario: Verify user has access to manage content -- Pathway "Post to Channel"
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with "Text" card
    And Verify that a card has been created
    And "Post to Channel" a card and then verify in a "TEST_AUTOMATION" channel
    Then Navigating to "DISCOVER" page
    And Verify in "TEST_AUTOMATION" channel
    And Verify that a card has been created and posted to the channel

  Scenario: Verify user has access to manage content -- "Delete posted card" from channel
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigating to "DISCOVER" page
    And Verify in "TEST_AUTOMATION" channel
    Then "Delete" a card from a channel

  Scenario: Verify that user able to use option Assign to Me card
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with "Text" card
    And Verify that a card has been created
    Then "Assign to Me" a piece of content
    And Verify "Assign to Me" option
    Then "Delete" a card

  Scenario: Verify user has access to manage content -- "Promote" a piece of new content and see it in "Featured"
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with "Text" card
    And Verify that a card has been created
    Then Verify "Promote" card feature
    And Navigate to "HOME" page "FEATURED" tab
    And Verify that a card has been promoted

  Scenario: Verify user has access to manage content -- "Unpromote" a piece of new content and see it in "Featured"
    Given Sign in as "existing user"
    And Navigate to "HOME" page "FEATURED" tab
    Then Verify "Unpromote" card feature
    And Navigate to "ME" page "Content" tab
    Then "Delete" a card







