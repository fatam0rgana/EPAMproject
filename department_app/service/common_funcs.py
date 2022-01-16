from department_app.models.department_model import Departments
from department_app.models.employee_model import Employees
import datetime


#function that counts amount of workers and their avg age for department
def count_avg_and_amount(dep):
    res = Employees.query.filter_by(emp_department = dep)
    sals = [x.emp_salary for x in res]
    try:
        return sum(sals)/len(sals), len(sals)
    except: 
        return 'No employees in department', 0


#function that gets employee's date of birth and counts his age
def count_age(emp):
    temp = datetime.datetime.strptime(Employees.query.filter_by(id = emp).first().emp_db, "%Y-%m-%d")
    today = datetime.date.today()
    return today.year - temp.year - ((today.month, today.day) < (temp.month, temp.day))


def get_all_deps():
    res = []
    for elem in Departments.query.all():
        res.append(elem.dep_name)
    return res
