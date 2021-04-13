import csv
with open('Internet Users.csv', newline="")as f:
    reader = csv.reader(f)
    file_data = list(reader)
    
    # to display no heading
    file_data.pop(0)
    print(file_data)