import datetime
import calendar

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def info(self):
        return f'имя:{self.name}; должность:{self.position}; зарплата:{self.salary}'

    def calc_salary(self, worked_days):
        return self.position * self.salary * worked_days


class Manager(Employee):
    def __init__(self, department, num_employees, name, position, salary):
        super().__init__(name, position, salary)
        self.department = department
        self.num_employees = num_employees


    def info(self):
        return f'имя:{self.name}; должность:{self.position}; зарплата:{self.salary}; депортамент:{self.department}; количество сотрудников: {self.num_employees}'

    def calc_salary(self, worked_days):
        return self.position * self.salary * worked_days + self.position * self.salary * worked_days * (1 / self.num_employees)




def worked_days():
    start_date = datetime.datetime.strptime("10/10/11", "20/03/2025")
        
    end_date = start_date + datetime.timedelta(days=5)
