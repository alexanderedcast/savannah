# Created by nik-edcast at 1/12/18
Feature: Verify follow and unfollow option

  """
  Follow and unfollow
  1. Return list of users that you already follow
  2. Go to Discover
  3. Then check if this user not in list of follower users
  4. Follow users and get name of this user
  5. Back to Me/Profile
  6. Check that you started follow
  """
  """
  These tests related to this ticket: - > https://jira.edcastcloud.com/browse/EP-10068
  """

  @BUG
  Scenario: Verify that possible to follow user from Discover
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigate to "ME" page "Profile" tab
    And Check the number "Following" users
    Then Navigating to "DISCOVER" page
    And "Follow" user from "Discover: People carousel"
    Then Navigate to "ME" page "Profile" tab
    Then Verify "Follow" action

  @BUG
  Scenario: Verify that possible to unfollow user from Discover
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigate to "ME" page "Profile" tab
    And Check the number "Following" users
    Then Navigating to "DISCOVER" page
    And "Unfollow" user from "Discover: People carousel"
    Then Navigate to "ME" page "Profile" tab
    Then Verify "Unfollow" action

  @BUG
  Scenario: Verify that possible to follow user from Profile page
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigate to "ME" page "Profile" tab
    And Check the number "Following" users
    Then Navigating to "DISCOVER" page
    And "Follow" user from "Discover: Profile page"
    Then Navigate to "ME" page "Profile" tab
    Then Verify "Follow" action

  @BUG
  Scenario: Verify that possible to unfollow user from Profile page
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigate to "ME" page "Profile" tab
    And Check the number "Following" users
    Then Navigating to "DISCOVER" page
    And "Unfollow" user from "Discover: Profile page"
    Then Navigate to "ME" page "Profile" tab
    Then Verify "Unfollow" action

  Scenario: Verify that possible to follow user from search
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigate to "ME" page "Profile" tab
    And Check the number "Following" users
    And "Follow" user from "Search"
    Then Navigate to "ME" page "Profile" tab
    Then Verify "Follow" action

  Scenario: Verify that possible to unfollow user from search
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigate to "ME" page "Profile" tab
    And Check the number "Following" users
    And "Unfollow" user from "Search"
    Then Navigate to "ME" page "Profile" tab
    Then Verify "Unfollow" action

  Scenario: Verify that possible to follow user from Me - Team
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigate to "ME" page "Profile" tab
    And Check the number "Following" users
    Then Navigate to "ME" page "Team" tab
    And "Follow" user from "Team"
    Then Navigate to "ME" page "Profile" tab
    Then Verify "Follow" action

  Scenario: Verify that possible to unfollow user from Me - Team
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigate to "ME" page "Profile" tab
    And Check the number "Following" users
    Then Navigate to "ME" page "Team" tab
    And "Unfollow" user from "Team"
    Then Navigate to "ME" page "Profile" tab
    Then Verify "Unfollow" action

  Scenario: Verify that possible to follow user from Leardboard
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigate to "ME" page "Profile" tab
    And Check the number "Following" users
    Then Navigate to "ME" page "Leaderboard" tab
    And "Follow" user from "Leader board"
    Then Navigate to "ME" page "Profile" tab
    Then Verify "Follow" action

  Scenario: Verify that possible to unfollow user from Leardboard
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Navigate to "ME" page "Profile" tab
    And Check the number "Following" users
    Then Navigate to "ME" page "Leaderboard" tab
    And "Unfollow" user from "Leader board"
    Then Navigate to "ME" page "Profile" tab
    Then Verify "Unfollow" action






