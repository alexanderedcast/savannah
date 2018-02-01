# Created by nik-edcast at 12/25/17
Feature: To verify that possible to create All types of card inside Journey

   Scenario: Verify that possible to create Link Journey
      Given Sign in as "existing user"
      And Verify the login has been "successful"
      Then Create "Journey" with "Link" card
      And Verify that a card has been created
      Then "Delete" a card from your content

   Scenario: Verify that possible to create Upload Journey
      Given Sign in as "existing user"
      And Verify the login has been "successful"
      Then Create "Journey" with "Upload" card
      And Verify that a card has been created
      Then "Delete" a card from your content

   Scenario: Verify that possible to create Poll Journey
    Given Sign in as "existing user"
      And Verify the login has been "successful"
      Then Create "Journey" with "Poll" card
      And Verify that a card has been created
      Then "Delete" a card from your content

   Scenario: Verify that possible to create Quiz Journey
      Given Sign in as "existing user"
      And Verify the login has been "successful"
      Then Create "Journey" with "Quiz" card
      And Verify that a card has been created
      Then "Delete" a card from your content

   # no ECL content > test fail
   @BUG
   Scenario: Verify that possible to create Dynamic Pathway Journey
      Given Sign in as "existing user"
      And Verify the login has been "successful"
      Then Create "Journey" with "Dynamic Pathway" card
      And Verify that a card has been created
      Then "Delete" a card from your content
   """
   As Like I have in my Expertise I have Python
   And I will bookmark card from Discover
   """
   # no ECL content > test fail
   @BUG
   Scenario: Verify that possible to create From Bookmark Journey
      Given Sign in as "existing user"
      And Verify the login has been "successful"
      Then Navigating to "DISCOVER" page
      And Pick some card and "Bookmark" and store title of this card
      Then Create "Journey" with "From Bookmark" card
      And Verify that a card has been created
      Then "Delete" a card from your content

    # no ECL content > test fail
   @BUG
   Scenario: Verify that possible to create Search SmartCard Journey
      Given Sign in as "existing user"
      And Verify the login has been "successful"
      Then Create "Journey" with "Search SmartCard" card
      And Verify that a card has been created
      Then "Delete" a card from your content

   Scenario: Verify that possible to create Text Journey
      Given Sign in as "existing user"
      And Verify the login has been "successful"
      Then Create "Journey" with "Text" card
      And Verify that a card has been created
      Then "Delete" a card from your content







