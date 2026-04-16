@sheet:ModelData
Feature: Model Integration Validation

Scenario Outline: Validate model behavior
  Given I load data for "<scenario_id>" "<test_case_id>"
   When I send data to model
   Then output should not be empty
   And output should be valid
   And output should be as expected
   And model output should be stored in DB
   And sensitive data should be masked
   Examples:
    | scenario_id | test_case_id |
    | SC01 | TC01 |
    | SC01 | TC02 |
    | SC02 | TC03 |
