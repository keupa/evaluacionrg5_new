from flask import Flask, render_template, request, redirect, url_for
from utils import convert_csv_to_json
import csv
from csv import writer

app = Flask(__name__,static_url_path="", template_folder='templates')

@app.route('/', methods=['GET'])
def home():
    response = convert_csv_to_json()
    return response

@app.route('/employee_table', methods=['GET'])
def show_employee_list():
    rows = []
    path = 'data/employees.csv'
    with open(path, 'r', encoding = "ISO-8859-1") as table:
        reader = csv.DictReader(table)
        for row in reader:
            rows.append(row)

    return render_template("table.html", rows=rows)

@app.route('/new_employee', methods=['GET', 'POST'])
def add_employee():
    path = 'data/employees.csv'
    if request.method == 'POST':
        employees = dict(request.form)
        first_name = employees['first_name']
        last_name = employees['last_name']
        email = employees['email']
        ip_address = employees['ip_address']

        employees = []

        with open(path, 'r') as table:
            reader = csv.reader(table)
            for row in reader:
                employees.append(row)

        with open(path, 'a', newline="", encoding="ISO-8859-1") as new_line:
            data = csv.writer(new_line)
            data.writerow([(int(row[0]) + 1), first_name, last_name, email, ip_address])
        return redirect(url_for('show_employee_list'))

    elif request.method == 'GET':
        return render_template("add.html")

# Call template for Error 404
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)