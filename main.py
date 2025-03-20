import datetime
import calendar
from employee import Employee, Manager  

def calculate_working_days_in_month(year, month):
    """
    рассчитывает количество рабочих дней (будней) в заданном месяце и году
    Учитывает только дни недели
    """
    num_working_days = 0
    for day in range(1, calendar.monthrange(year, month)[1] + 1):  # [1] - количество дней в месяце
        date = datetime.date(year, month, day)
        if date.weekday() < 5:  # 0-4: Пн-Пт
            num_working_days += 1
    return num_working_days

if __name__ == "__main__":
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    worked_days = calculate_working_days_in_month(current_year, current_month)

    name1 = input('Напишите имя сотрудника: ')
    pos = float(input('Введите коофицент должности сотрудника: '))
    sal = float(input('Введите зарплату сотрудника: '))

    Emp = Employee(name1, pos, sal)
    print(f'Информация о сотруднике: {Emp.info()}')
    print(f'Зарплата сотрудника: {Emp.calc_salary(worked_days)}')  # Выводим получку!!!


    print(f'Информация о сотруднике: {Emp.info()}')


    department = input('Напишите название департамента: ')
    num = int(input('Введите количество сотрудников: '))
    name2 = input('Напишите имя менеджера: ')
    pos1 = float(input('Введите коофицент должности менеджера: '))
    sal1 = float(input('Введите зарплату менеджера: '))


    man = Manager(department, num, name2, pos1, sal1, worked_days)

    print(f'Информация о менеджере: {man.info()}')
    print(f'Зарплата менеджера: {man.calc_salary()}')
