import pandas
import datetime



class employee:
    employees = ["виктор, сергеич, петрович, вовчик"]
    def __init__(self, name, position, salari):
        self.name = str(name)
        self.position = int(position)
        self.salari = int(salari) 

    def info(self):
        return employee    (self.name) + " " + (self.position) + " " + (self.salari)
    
    
    


    def calc_salari(self):
        return employee  (self.position)*(self.salari)*worked_days
 


class manager(employee):
    def __init__(self, department,num_employee):
        self.department = department
        self.num_employee = num_employee




def worked_days():
    start_date = datetime.datetime.strptime("10/10/11", "20/03/2025")
        
    end_date = start_date + datetime.timedelta(days=5)