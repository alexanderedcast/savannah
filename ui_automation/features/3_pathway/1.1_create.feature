Feature: Verify that possible to create a Pathway with optional options

  Scenario: Verify that possible to create Pathway and provide description
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with any card and "description"
    And Verify that a card has been created
    Then Verify that this "Pathway" has been created with "description"
    Then "Delete" a card from your content

  Scenario: Verify that possible to create Pathway and post to channel
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with any card and "post to channel"
    And Verify that a card has been created
    Then Verify that this "Pathway" has been created with "post to channel" option

  Scenario: Verify that possible to create Pathway with level of complexity
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with any card and "level of complexity"
    And Verify that a card has been created
    Then Verify that this "Pathway" has been created with "level of complexity" option
    Then "Delete" a card from your content

  Scenario: Verify that possible to create Pathway with tag
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with any card and "add tag"
    And Verify that a card has been created
    Then Verify that this "Pathway" has been created with "add tag" option
    Then "Delete" a card from your content

  Scenario: Verify that possible to create Pathway with banner
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with any card and "banner"
    And Verify that a card has been created
    Then "Delete" a card from your content

  Scenario: Verify that possible to create Pathway after draft
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Create "Pathway" with any card and "after draft"
    And Verify that a card has been created
    Then Verify that this "Pathway" has been created with "draft" option
    Then "Delete" a card from your content






