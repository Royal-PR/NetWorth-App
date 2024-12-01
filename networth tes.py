import csv

def get_row():
    with open("rows.csv", "r", newline="") as file:
        reader = csv.reader(file)
        data = []
        for row in reader:
            data.append(row)
        return data

print(get_row())


def write_heading(new_heading):
    with open("headings.csv", "a+", newline="") as file:
        headings = csv.reader(file)
        headings.append(new_heading)
        headings.

write_heading("Mar")