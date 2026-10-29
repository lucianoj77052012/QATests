# QATests
A collection of tests aimed at ensuring automation practice sites work as expected both from front end and back end perspectives.

# HOW TO BUILD

You will need api_keys.txt with the corresponding keys.

Install Docker at https://docs.docker.com/desktop/setup/install/windows-install/ (for Windows). Make sure the daemon is running (opening Docker Desktop runs it). Then run:

`docker build -t qatests .`

And:

`docker run -v ./reports:/usr/src/app/reports qatests`

The -v option makes it such that the screenshots taken (reports) are saved into the host machine.

# ABOUT THE HOTEL APP

It's an app where you can book your stays in a room within a property.

It is meant for testing purposes only -- booking a stay doesn't actually book anything from a production standpoint.

# PROJECT STRUCTURE

There are four main directories, described in the table below:

| Directory     | Contents 
|---------------|----------
| test_cases    | *.feature files written in Gherkin language. Non-programmers users can focus on writing them without the need to ever write a single line of code. 
| test_data     | *.csv files to test different scenarios with different data. We can add more data without the need to duplicate scenarios.
| test_steps    | *.py files with the code implementation of the Gherkin phrases. Programmers can add new code as needed.
| test_execute  | *.py files that are the entry point to each test.

In addition, `conftest.py` holds the fixtures required for the tests to work (for frontend tests for example, a browser fixture makes it accessible to all tests).

# BACKEND AND FRONTEND TESTS

Each of the four directories described above holds both a backend and a frontend directory (along with a separate login directory, which is performed only via frontend
since for the backend authentication is performed via the api_key).

Frontend tests are directed towards testing UI fields: required fields, toast messages, etc. A browser running in headless mode is used.
Backend tests are directed towards API actions: validating the response after a request contains valid data and follow business rules.

# LICENSE

See LICENSE for details.