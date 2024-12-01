table_headings = ["Accounts","Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

rows = [["Barclays Checking", "100", "150","200"],
        ["Barclays Saving", "500", "150", "130"],
        ["MoneyBox LISA", "500", "150", "50"]]

jan_total =sum(int(item[1]) for item in rows)

print(jan_total)