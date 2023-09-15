import time
import random
from faker import Faker
from libs.api_helpers.employee_api import EmployeeApi
from libs.builders.employee_builder import EmployeeBuilder
from assertpy import assert_that
from text_resources.employee import EmployeeTexts
from http import HTTPStatus


fake = Faker()

client = EmployeeApi()

class TestCreateEmployee:
    def test_create_employee_should_return_201_when_all_fields_are_valid(self):
        # Arrange
        employee_payload = EmployeeBuilder()\
            .setName(fake.name())\
            .setAge(str(random.randint(18, 100)))\
            .setSalary(str(random.randint(500, 1000000)))\
            .build()
        # Act
        create_empl_res = client.create_employee(employee_payload)
        # Assertion
        assert_that(create_empl_res.status_code).is_equal_to(HTTPStatus.OK)
        assert_that(create_empl_res.json()['message']).is_equal_to(EmployeeTexts.created_item)
        assert_that(create_empl_res.json()['status']).is_equal_to('success') # Can use enum if we have multiple statuses, skip for now
        assert_that(create_empl_res.json()['data']).is_equal_to(employee_payload, include=['name', 'age', 'salary'])

        # Get created employee's id
        time.sleep(60) # Sleep 60 secs to prevent error: too many request when calling api consequence
        employee_id = create_empl_res.json()['data']['id']
        get_empl_res = client.get_employee(employee_id)
        assert_that(get_empl_res.status_code).is_equal_to(HTTPStatus.OK)
        assert_that(get_empl_res.json()['status']).is_equal_to('success')
        assert_that(get_empl_res.json()['data']).is_none()
        assert_that(get_empl_res.json()['message']).is_equal_to(EmployeeTexts.item_fetched)

        # Clean up data (delete created employee -> can add in setup, teardown) in fixture (or reset db after all test runs)