from libs.api_helpers.base_api import BaseApi


class EmployeeApi(BaseApi):
    def __init__(self) -> None:
        super().__init__()
        # Due to error Python Requests HTTP Response 406, So need to add a User-Agent here to solve problem
        # The default Python User-Agent 'python-requests/2.21.0' was being probably blocked by the hosting company
        self.headers = {
            'User-Agent': 'AUTO_TEST'
        }

    def list_employees(self):
        return self.get('/employees', headers=self.headers)

    def create_employee(self, payload = None):
        return self.post('/create', data=payload, headers=self.headers)
    
    def get_employee(self, id):
        return self.get(f'/employee/{id}', headers=self.headers)
        