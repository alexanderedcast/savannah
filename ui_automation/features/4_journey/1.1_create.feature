# Created by nik-edcast at 12/26/17
Feature: Verify that possible to create a Journey with optional option

  Scenario: Verify that possible to create Journey and provide description
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Journey" with any card and "description"
    Then Verify that this "Journey" has been created with "description" option
    Then "Delete" a card from your content

  Scenario: Verify that possible to create Journey and post to channel
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Journey" with any card and "post to channel"
    And Verify that a card has been created
    Then Verify that this "Journey" has been created with "post to channel" option
    Then "Delete" a card from your content

  Scenario: Verify that possible to create Journey with level of complexity
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Journey" with any card and "level of complexity"
    And Verify that a card has been created
    Then Verify that this "Journey" has been created with "level of complexity" option
    Then "Delete" a card from your content

  Scenario: Verify that possible to create Journey with tag
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Journey" with any card and "add tag"
    And Verify that a card has been created
    Then Verify that this "Journey" has been created with "add tag" option
    Then "Delete" a card from your content

  Scenario: Verify that possible to create Journey with banner
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Journey" with any card and "banner"
    And Verify that a card has been created
    Then "Delete" a card from your content

  Scenario: Verify that possible to create Journey after draft
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Journey" with any card and "after draft"
    And Verify that a card has been created
    Then Verify that this "Journey" has been created with "draft" option
    Then "Delete" a card from your content
