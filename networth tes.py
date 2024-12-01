import FreeSimpleGUI as sg


def get_row():
    # Replace with your logic to get table rows
    return [["Row1 Col1", "Row1 Col2"], ["Row2 Col1", "Row2 Col2"]]


def get_heading():
    # Replace with your logic to get table headings
    return ["Column1", "Column2"]


def write_heading(headings):
    # Replace with your logic to save updated headings
    print("Updated Headings:", headings)


# Function to create the window
def create_window(headings, rows):
    table = sg.Table(values=rows, headings=headings, key="table", enable_events=True)
    layout = [
        [table],
        [sg.Input(key="input_month"), sg.Button("Add Month", key="add_month")],
    ]
    return sg.Window("Test Table Update", layout, finalize=True)


# Initial data
table_headings = get_heading()
table_rows = get_row()
window = create_window(table_headings, table_rows)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "add_month":
        new_month = values.get("input_month")
        if new_month:
            table_headings.append(new_month)
            write_heading(table_headings)

            # Close the current window and recreate it with updated headings
            window.close()
            window = create_window(table_headings, table_rows)