import csv

with open('./data/demo_invoices4.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        try:
            print(row)
            print(f"Amount: {row['amount']}")
            float_amount = float(row['amount'])
            print(type(float_amount))
        except ValueError as e:
            print(f"Error: Column {e} not found in row")
        except KeyError as e:
            print(f"Error: Column {e} not found in row")
