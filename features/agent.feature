@sheet:AgentData
Feature: Agent Data Extraction and Validation

Scenario Outline: Validate end-to-end data flow
  Given I load data for "<scenario_id>" "<test_case_id>"
   When I validate data
   Then validation result should be as expected
   When I call backend
   And data should be stored in DB
   And sensitive data should be masked
   Examples:
    | scenario_id | test_case_id |
    | SC01 | TC01 |
    | SC01 | TC02 |
    | SC02 | TC03 |
    | SC02 | TC04 |