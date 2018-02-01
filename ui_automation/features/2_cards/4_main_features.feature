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

  Scenario: Verify post like feature SmartCard
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    When Create "SmartCard" with "Text" card
    And Verify that a card has been created
    Then Leave a "like" on the card and verify the "post" action

  Scenario: Verify remove like feature SmartCard on Me - Content
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    And Navigate to "ME" page "Content" tab
    Then Leave a "like" on the card and verify the "remove" action
    And "Delete" a card from your content

  Scenario: Verify leave comment feature SmartCard
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    When Create "SmartCard" with "Text" card
    And Verify that a card has been created
    Then "Leave" a "comment" for SmartCard

  Scenario: Verify delete comment feature SmartCard
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    And Navigate to "ME" page "Content" tab
    Then "Delete" a "comment" for SmartCard
    And "Delete" a card from your content

  Scenario: Verify mark as completed feature on Me content
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    When Create "SmartCard" with "Text" card
    And Verify that a card has been created
    Then Verify that possible to "completed" a SmartCard
    And "Delete" a card from your content

  Scenario: Verify comment statistics feature in SmartCard
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    When Create "SmartCard" with "Text" card
    And Verify that a card has been created
    Then "Leave" a "comment" for SmartCard
    And Verify "comments_count" in "statistics"
    And "Delete" a card from your content

  Scenario: Verify like statistics feature in SmartCard
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    When Create "SmartCard" with "Text" card
    And Verify that a card has been created
    Then Leave a "like" on the card and verify the "post" action
    And Verify "likes_count" in "statistics"
    And "Delete" a card from your content

  Scenario: Verify completed statistics feature in SmartCard
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    When Create "SmartCard" with "Text" card
    And Verify that a card has been created
    Then Verify that possible to "completed" a SmartCard
    And Verify "completes_count" in "statistics"
    And "Delete" a card from your content

  Scenario: Verify bookmark statistics feature in SmartCard
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    When Create "SmartCard" with "Text" card
    And Verify that a card has been created
    Then "Bookmark" a content
    And Verify "bookmarks" in "statistics"
    And "Delete" a card from your content

    # Views statistic
















