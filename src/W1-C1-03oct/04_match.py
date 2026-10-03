file = "csv"
count = 50
if file == "csv":
    print("You have selected CSV file format")
elif file == "json":
    print("You have selected JSON file format")
elif file == "xml":
    print("You have selected XML file format")
else:
    print("Invalid file format selected")

### Match Statement for better performance and readability
match file:
    case "csv": 
        print("You have selected CSV file format")
    case "json":
        print("You have selected JSON file format")
    case "xml":
        print("You have selected XML file format")
    case _:
        print("Invalid file format selected")


if (file == "csv" or file == "xlsx" or file == "xls") and count >= 50:
    print("You have selected CSV or Excel file format")


