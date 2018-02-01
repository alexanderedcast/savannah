# Created by nik-edcast at 12/19/17
Feature: Pathway Creation
"""Verify that user can create Pathway"""
  """
  1. Login
  2. Create Pathway
  3. Verify creation
  4. Delete card
  """
  Scenario: Verify that possible to create Link Pathway
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with "Link" card
    And Verify that a card has been created
    Then "Delete" a card from your content

  Scenario: Verify that possible to create Upload Pathway
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with "Upload" card
    And Verify that a card has been created
    Then "Delete" a card from your content

  Scenario: Verify that possible to create Poll Pathway
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with "Poll" card
    And Verify that a card has been created
    Then "Delete" a card from your content

  Scenario: Verify that possible to create Quiz Pathway
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with "Quiz" card
    And Verify that a card has been created
    Then "Delete" a card from your content

  # no ECL content > test fail
   @BUG
  Scenario: Verify that possible to create Dynamic Pathway Pathway
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with "Dynamic Pathway" card
    And Verify that a card has been created
    Then "Delete" a card from your content

  """
  As Like I have in my Expertise I have Python
  And I will bookmark card from Discover
  """
   # no ECL content > test fail
   @BUG
  Scenario: Verify that possible to create From Bookmark Pathway
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigating to "DISCOVER" page
    And Pick some card and "Bookmark" and store title of this card
    Then Create "Pathway" with "From Bookmark" card
    And Verify that a card has been created
    Then "Delete" a card from your content

   @BUG
  Scenario: Verify that possible to create Search SmartCard Pathway
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with "Search SmartCard" card
    And Verify that a card has been created
    Then "Delete" a card from your content

  Scenario: Verify that possible to create Text Pathway
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with "Text" card
    And Verify that a card has been created
    Then "Delete" a card from your content







