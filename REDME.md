# Getting Started With Selenium Testing With Python and Pytest Framework

## Prerequisites

Before you can start performing Python 3 automation testing using pytest, you would need to:

1. Install the latest Python Interpreter from the official website. We recommend using the latest version.
2. Install the latest version of Pycharm IDE

## Installation
1. Install Selenium through pip command:
```bash
pip install selenium
```

2. As the pytest is not a part of the standard Python library, it needs to be installed separately. To install pytest, you have to execute the following command on the terminal (or command prompt) that makes use of the Python package manager (pip):

```bash
pip install pytest
```
3. For html report install pytest-html.
```bash
pip install pytest-html
```

4. For allure report install allure-pytest:
```bash
pip install allure-pytest
```
## Execution
The following command is executed on the terminal after navigating to the directory that contains the test code.

1. For running Login test file with generating html report
```bash
run pytest test_LoginPage.py -v --capture=tee-sys --html=Reports/Login.html
```
2. For running SignUp test file with generating html report
```bash
run pytest test_Cases.py -v --capture=tee-sys --html=Reports/signup.html
```
3. For running All test cases file
```bash
run pytest -v --capture=tee-sys --html=Reports/AllTestcases.html
```
4. To generate html file
```bash
run pytest -v --capture=tee-sys 
```
5. To generate allure report
```bash
run pytest -v --capture=tee-sys --alluredir="C:\ProgramData\Jenkins\.jenkins\jobs\Pytest_Demo\SyllabyProjectNew
\AllureReports"
```
then copy the path of the AllureReports and open Command Prompt:
```bash
run allure serve "path of the allure report folder[C:\ProgramData\Jenkins\.jenkins\jobs\Pytest_Demo\SyllabyProjectNew
\AllureReports]"
```

# Jenkins CI with PyTest
## How it works
1. First, I run the tests on local environment, then started building a CI pipeline.
2. I have installed Jenkins server (installed suggested plugins), Python Plugin, Selenium Plugin, Allure Jenkins Plugin and HTML Publisher Plugin.
3. Created a freestyle job.
4. Setting up build steps and Save it.
```bash
call ./venv/Scripts/activate.bat
cd PytestFramework/Tests_Suits
pytest -v --capture=tee-sys --alluredir="C:\ProgramData\Jenkins\.jenkins\jobs\Pytest_Demo\SyllabyProjectNew\AllureReports" 

```
5. Press build now, to run the job, then go inside the job and check build history.