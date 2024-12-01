import FreeSimpleGUI as sg
import csv


# DO NOT DELETE ~ code to calculate sum of a column (will need this later when totalling savings):
#   jan_total =sum(int(item[1]) for item in rows)

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






#-------------------------------------


# input buttons
add_new_month = sg.Input(tooltip="enter the next month", key="input_month")
button = sg.Button("add month", key="add_month")

add_new_bchecking = sg.Input()
button2 = sg.Button("Add Barclays Checking")

add_new_bsaving = sg.Input()
button3 = sg.Button("Add Barclays savings")

add_new_mbox_lisa = sg.Input()
button4 = sg.Button("Add MoneyBox LISA")


#table
table = sg.Table(values=get_row(), headings=get_heading(), key="table")

#window layout
window = sg.Window("test", layout=[[table],
                                   [add_new_month, button],
                                   [add_new_bchecking, button2],
                                   [add_new_bsaving, button3],
                                   [add_new_mbox_lisa, button4]])

while True:
    event, values = window.read()
    match event:
        case "add_month":
            headings = get_heading()
            headings.append(values["input_month"])
            write_heading(headings)
            #table_updater = []
            #table_updater.append(headings)
            #window["table"].update()



window.close()
