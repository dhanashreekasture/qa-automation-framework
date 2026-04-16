# qa-automation-framework
Selenium Python Automation Framework using BDD (Behave), Page Object Model, API utilities, and reusable components with logging, retry, and reporting.

# QA Automation Framework 

## Overview
This is a BDD-based automation framework built using:
* Python
* Behave (BDD)
* Selenium (UI)
* API testing (requests)
* PostgreSQL DB validation


## Features
* Data-driven testing using Excel
* Dynamic payload builder
* Environment-based execution (dev/qa/uat/prod)
* API + UI + Model validation
* Page Object Model (POM)
* Retry mechanism for flaky tests
* Screenshot capture on failure
* CI/CD ready (Docker + Jenkins)
* Allure reporting


## Project Structure
* `features/` → BDD feature files & steps
* `pages/` → UI Page Objects
* `utils/` → reusable utilities
* `config/` → environment config
* `data/` → test data


## Virtual Env Setup
1] Create virtual environment
   python -m venv venv
2] Activate virtual environment
   venv\Scripts\activate
3] Install dependencies
pip install -r requirements.txt


## Run Tests
behave -D env=qa


## Run with Allure Report
behave -D env=qa -f allure_behave.formatter -o reports/allure-results
allure serve reports/allure-results


## Environment Configuration
Use `.env` file 


## CI/CD
* Docker supported
* Jenkins pipeline included


## Author
Dhanashree K
