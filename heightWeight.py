import csv
with open('SOCR-HeightWeight.csv') as f:
    reader = csv.reader(f) 
    file_data = list(reader)

from collections import Counter
new_data = "whitehatJR"
data = Counter(new_data)
print(data)

new_list = data.items()
print(new_list)

new_values = data.values()
print(new_values)