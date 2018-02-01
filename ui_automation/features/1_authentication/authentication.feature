Feature: Authentication
"""Verify the sign in and sign out options"""
  """
  1. Login
  2. Verify the action
  3. If need to, log out
  """
  Scenario: Verify that user can sign in if account exist in system
    Given Sign in as "existing user"
    And Verify the login has been "successful"

  """
  @EP-8116
  """
  @BUG
  Scenario: Verify that user can finish session using the Sign out option
    Given Sign in as "existing user"
    And Verify the login has been "successful"
    Then Do "Sign Out" from the system

  """
  # Some problem with automation
  2 factor authentication
  """
  @BUG
  Scenario: Verify that user can log in using Facebook SSO
    Given Log in with "Facebook" SSO
    And Sign in as "sso user" with "any" role
    Then Verify the login has been "successful"
  """
  # Some problem with automation
  2 factor authentication
  """
  @BUG
  Scenario: Verify that user can log in using Google SSO
    Given Log in with "Google" SSO
    And Sign in as "sso user" with "any" role
    Then Verify the login has been "successful"

  """
  Some problem with automation
  2 factor authentication
  """
  @BUG
  Scenario: Verify that user can log in using LinkedIn SSO
    Given Log in with "LinkedIn" SSO
    And Sign in as "sso user" with "any" role
    Then Verify the login has been "successful"

  Scenario: Verify that user can restore password using restore option
    Given Sign in as "user what need to restore password" with as has member role
    Then Verify the login has been "invalid"
    And Reset my password
    Then Verify the login has been "successful"
