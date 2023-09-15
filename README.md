# rest_api_project
Setup environment
1. Install python & pip
    By default, after installed python you already have pip installed
    I'm using python version `3.11.5` and pip version `23.2.1`
2. Install pipenv
    Run `pip install pipenv`

3. Clone the project
    git clone `https://github.com/longnv1995/rest_api_project.git`
4. Go to the `root` project folder (rest_api_project) 
    Run `pipenv install`
By running above command, it will install all packages from Pipfile
5. To activate virtual env by running `pipenv shell`
6. To exit virtual env, type `exit`

How to run the tests
To run specific test file
Run `pytest 'path/to/the/test/file' -v -s`
Ex: `pytest test_suites\employees\test_create_employee.py -v -s`