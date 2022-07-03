Feature: Search

  Scenario: Login
    Given I navigate to the Google website
    When I enter "python behave" in the search bar and click search
    Then I can see results related to "python behave"
