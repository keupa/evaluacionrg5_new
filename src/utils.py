import csv
from flask import jsonify

def convert_csv_to_json():
    path = 'data/employees.csv'
    with open (path, 'r') as file:
        reader = csv.reader(file)
        data_list = list()
        for row in reader:
            data_list.append(row)
        data = [dict(zip(data_list[0],row)) for row in data_list]
        data.pop(0)
        s = jsonify(data)
        return s
