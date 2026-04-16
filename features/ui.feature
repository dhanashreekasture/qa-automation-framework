@ui
Feature: File Upload Validation

  Scenario: Upload invalid file
    Given user opens application
    When user uploads invalid file
    Then error message should appear