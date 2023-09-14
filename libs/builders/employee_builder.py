class EmployeeBuilder:
    def __init__(self) -> None:
        self._name = None
        self._salary = None
        self._age = None

    def setName(self, name):
        self._name = name
        return self
    
    def setSalary(self, salary):
        self._salary = salary
        return self
    
    def setAge(self, age):
        self._age = age
        return self
    
    def build(self):
        return {
            "name": self._name,
            "salary": self._salary,
            "age": self._age
        }
    

