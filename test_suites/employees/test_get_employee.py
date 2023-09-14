from libs.api_helpers.employee_api import EmployeeApi
from http import HTTPStatus
from text_resources.employee import EmployeeTexts
from assertpy import assert_that

from utils.helpers import filter_by


client = EmployeeApi()

class TestCreateEmployee:
    def test_get_employees_matched_age_is_greater_than_60_and_salary_is_greater_than_300000(self):
        # Act
        employees_res = client.list_employees()
        # Assertion
        assert_that(employees_res.status_code).is_equal_to(HTTPStatus.OK)
        assert_that(employees_res.json()['status']).is_equal_to('success') # Can use enum if we have multiple statuses, skip for now
        assert_that(employees_res.json()['message']).is_equal_to(EmployeeTexts.all_items_fetched)
        assert_that(employees_res.json()).contains_only('status', 'data', 'message')
        # Print results after filtered
        print(filter_by(age=60, salary=300000, list_items=employees_res.json()['data']))
