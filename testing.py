import csv

# Data to write to file
data = [
    ["Accounts", "Jan", "Feb"],
]

# Open the file for writing
with open("headings.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)