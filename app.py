from flask import Flask, render_template, url_for, flash, request


app = Flask(__name__)
app.config['SECRET_KEY'] = "adnjkfvfdankvfadkb"


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


@app.route("/add_employee", methods = ['POST', 'GET'])
def add_employee():
    if request.method == 'POST':
        if len(request.form['employee_name']) > 0:
            flash(f"{request.form['employee_name']} added", 'alert-success')
        else:
            flash('error', 'alert-danger')
    return render_template('add_employee.html', menu = menu, dropdown = dropdown, title = 'Add employee')


@app.route("/add_department", methods = ['POST', 'GET'])
def add_department():
    if request.method == 'POST':
        if len(request.form['department_name']) > 0:
            flash(f"{request.form['department_name']} added", 'alert-success')
        else:
            flash('error', 'alert-danger')
    return render_template('add_department.html', menu = menu, dropdown = dropdown, title = 'Add department')


if __name__ == '__main__':
    app.run(debug=True)
