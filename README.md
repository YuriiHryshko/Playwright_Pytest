## Summary of Repo

This repository contains automated tests using the Playwright and Pytest.

[Tested website](https://www.automationexercise.com)

[Test cases](https://www.automationexercise.com/test_cases)

## Requirements

Before running the tests, you need to have the following software and dependencies installed:

- Python
- Allure Report

## Steps to Install
1. Clone this repository to your local machine:
    ```
    git clone https://github.com/YuriiHryshko/Playwright_Pytest.git
    ```
2. Navigate to the project folder:
    ```
    cd Playwright_Pytest
    ```
3. Install the required dependencies:
    ```
    python -m pip install --upgrade pip
    pip install pipenv
    pipenv install --system
    playwright install chromium
    ```
## Steps to Run Tests

Running all tests:
```
pytest
```
Running a particular test:
```
pytest -k <test_name>
```
## Steps to Create the Report
The test report is generated automatically after running the tests. After running the tests, execute the following command to open the report:
```
allure serve reports
```