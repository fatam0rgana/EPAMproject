from flask import Flask, render_template, url_for
app = Flask(__name__)

menu = [{'name': 'Departments', 'url': 'departments'},{'name': 'Employees', 'url': 'employees'}]
dropdown = [{'name': 'Add department', 'url': 'add_department'},{'name': 'Add employee', 'url': 'add_employee'}]
@app.route("/")
def index():
    return render_template('index.html', menu = menu, dropdown = dropdown, title = 'Homepage')

@app.route("/departments")
def departments():
    return render_template('departments.html', menu = menu, dropdown = dropdown, title = 'Departments')

@app.route("/employees")
def employees():
    return render_template('employees.html', menu = menu, dropdown = dropdown, title = 'Employees')

@app.route("/add_employee")
def add_employee():
    return render_template('add_employee.html', menu = menu, dropdown = dropdown, title = 'Add employee')

@app.route("/add_department")
def add_department():
    return render_template('add_department.html', menu = menu, dropdown = dropdown, title = 'Add department')

if __name__ == '__main__':
    app.run(debug=True)
