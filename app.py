from flask import Flask, render_template, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy

#setting configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = "adnjkfvfdankvfadkb"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sql/department.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#creating db
db = SQLAlchemy(app)

class Departments(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    dep_name = db.Column(db.String(50), nullable = False, unique = True)
    dep_description = db.Column(db.String(150))


class Employees(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    emp_name = db.Column(db.String(50), nullable = False)
    emp_db = db.Column(db.String, nullable = False)
    emp_salary = db.Column(db.Integer, nullable = False)
    emp_department = db.Column(db.String(50), nullable = False)

def count_avg(dep):
    res = Employees.query.filter_by(emp_department = dep)
    sals = [x.emp_salary for x in res]
    try:
        return sum(sals)/len(sals)
    except: 
        return 'No employees in department'


#variables for html
menu = [{'name': 'Departments', 'url': 'departments'},{'name': 'Employees', 'url': 'employees'}]
dropdown = [{'name': 'Add department', 'url': 'add_department'},{'name': 'Add employee', 'url': 'add_employee'}]

#app routes for links
@app.route("/")
def index():
    return render_template('index.html', menu = menu, dropdown = dropdown, title = 'Homepage')


@app.route("/departments")
def departments():
    return render_template('departments.html', all_deps = Departments.query.all(), salarys = {elem.dep_name: count_avg(elem.dep_name) for elem in Departments.query.all()}, menu = menu, dropdown = dropdown, title = 'Departments')


@app.route("/employees")
def employees():
    return render_template('employees.html', all_emps = Employees.query.all(), menu = menu, dropdown = dropdown, title = 'Employees')


@app.route("/add_employee", methods = ['POST', 'GET'])
def add_employee():
    if request.method == 'POST':
        try:
            new_emp = Employees(emp_name = request.form['employee_name'], emp_db = request.form['employee_age'], emp_salary = request.form['employee_salary'], emp_department = request.form['employee_department'])
            db.session.add(new_emp)
            db.session.flush()
            db.session.commit()
            flash(f"{request.form['employee_name']} added", 'alert-success')
        except:
            db.session.rollback()
            flash('error', 'alert-danger')
    return render_template('add_employee.html', all_deps = Departments.query.all(), menu = menu, dropdown = dropdown, title = 'Add employee')


@app.route("/add_department", methods = ['POST', 'GET'])
def add_department():
    if request.method == 'POST':
        try:
            new_dep = Departments(dep_name = request.form['department_name'], dep_description = request.form['department_description'])
            db.session.add(new_dep)
            db.session.flush()
            db.session.commit()
            flash(f"{request.form['department_name']} added", 'alert-success')
        except:
            db.session.rollback()
            flash('error', 'alert-danger')
    return render_template('add_department.html', menu = menu, dropdown = dropdown, title = 'Add department')
    

if __name__ == '__main__':
    app.run(debug=True)
