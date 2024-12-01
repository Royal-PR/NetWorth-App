import FreeSimpleGUI as sg

# data for table headings and rows
table_headings = ["Accounts","Jan", "Feb", "Mar"]
rows = [["Barclays Checking", "100", "150","200"],
        ["Barclays Saving", "500", "150", "130"],
        ["MoneyBox LISA", "500", "150", "50"],
        ["Total"]]



# input buttons
add_new_month = sg.Input()
button = sg.Button("add month")

add_new_bchecking = sg.Input()
button2 = sg.Button("Add Barclays Checking")

add_new_bsaving = sg.Input()
button3 = sg.Button("Add Barclays savings")

add_new_mbox_lisa = sg.Input()
button4 = sg.Button("Add MoneyBox LISA")


#table
month = sg.Table(values=rows, headings=table_headings)

#window layout
window = sg.Window("test", layout=[[month],
                                   [add_new_month, button],
                                   [add_new_bchecking, button2],
                                   [add_new_bsaving, button3],
                                   [add_new_mbox_lisa, button4]])
window.read()
window.close()
