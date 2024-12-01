import FreeSimpleGUI as sg
import csv


# DO NOT DELETE ~ code to calculate sum of a column (will need this later when totalling savings):
#   jan_total =sum(int(item[1]) for item in rows)

# WHATS NEXT? Finish the table updater so it shows the update for a new month as soon as you add the month.


#Functions
def get_heading():
    with open("headings.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
                return row


def write_heading(new_heading):
    with open("headings.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(new_heading)


def get_row():
    with open("rows.csv", "r", newline="") as file:
        reader = csv.reader(file)
        data = []
        for row in reader:
            data.append(row)
        return data

def create_table():
    return sg.Table(
        values=get_row(),
        headings=get_heading(),
        key="table",
        enable_events=True,
        auto_size_columns=True
    )

#-------------------------------------

# input buttons/variables
add_new_month = sg.Input(tooltip="enter the next month", key="input_month")
button = sg.Button("add month", key="add_month")

add_new_bchecking = sg.Input()
button2 = sg.Button("Add Barclays Checking")

add_new_bsaving = sg.Input()
button3 = sg.Button("Add Barclays savings")

add_new_mbox_lisa = sg.Input()
button4 = sg.Button("Add MoneyBox LISA")

#initial table
table = create_table()

layout = [[table],
          [add_new_month, button],
          [add_new_bchecking, button2],
          [add_new_bsaving, button3],
          [add_new_mbox_lisa, button4]]


#window layout
window = sg.Window("test", layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    match event:
        case "add_month":
            # Add the new month to headings
            new_month = values.get("input_month")
            if new_month:
                headings = get_heading()
                headings.append(new_month)
                write_heading(headings)


window.close()
