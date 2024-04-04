A front-end Python automation framework for testing user journeys at https://www.saucedemo.com

This framework makes use of an example website to run BDD style scenarios via automation using Python and the following libraries:

Selenium Web Driver
Behave

The repo includes a feature file for test scenarios in Cucumber format, an underlying step definition file for executing the tests, <br>
and You will need a Gitbash or Unix based terminal before walking through the installation listed below.

Setup checklist
Clone the repository
Download Chrome
Download Python 3
Install requirements
Run the test scenarios
Optional: Reporting



Python 3
Please ensure that Python 3 is installed on your machine. You can check in a bash shell or command prompt by running:

python3 --version
The downloads can be found at https://www.python.org/downloads/

Install requirements
After installing the repo and Python 3, the required dependencies need to be installed within the project folder by running:

pip install -r requirements.txt
If you have trouble with pip or from pre-existing packages, try installing just within the module itself:

python3 -m pip install -r requirements.txt
Run the test scenarios
Once you have the repo, Chrome, Python 3 and have installed the requirements, simply run the following from the same directory:

behave
The test framework should start running and you will see a web driver opening Chrome and automating tests.

Test reports
-- OPTIONAL
By default, the test framework uses Behave's logger to print results in the console, and also write custom logging to logs/demo.log. <br>
If you would like to install a web app to open and view comprehensive test reports from within a browser, you will need to have npm installed and allure-behave.

