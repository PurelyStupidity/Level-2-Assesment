import csv
import rich
from rich.console import Console
from rich import print
from rich.table import Table

choice = ""
item_list = []

console = Console()


def check_float(question):
    while True:
        try:
            float_num = console.input(question)  # ask question
            return float(float_num)  # convert to float and return it
        except ValueError:  # if not a float then ask again
            console.print("Please enter a valid number", style="underline bold red")


def Check_Blank(question):
    while True:
        text = input(question)  # ask question
        if (
            text != "" and text.isnumeric() == False
        ):  # if text isn't empty then return it
            return text
        else:  # if text is empty then ask again
            console.print("Please enter a valid name.", style="underline bold red")


def get_unit():
    while True:
        unit = input("Enter the unit\nKg, L, ml, g: ").lower()
        if unit not in ["kg", "l", "ml", "g"]:
            console.print("\nInvalid unit\n", style="underline bold red")
        else:
            break

    while True:
        amount = input("Enter the amount: ")
        if amount.isnumeric():
            break
        else:
            print("\nInvalid amount\n")
    if unit in ["ml", "g"]:
        amount = int(amount) / 1000
    return unit, amount


def check_price():
    while True:
        try:
            price = float(input("Enter the price: $"))
            return price
        except ValueError:
            console.print("\nInvalid price\n", style="underline bold red")


def append_list(Item, Unit, Weight, Price):
    # append items to Items.csv
    data = {
        "Item": Item,
        "Unit": Unit,
        "Weight": Weight,
        "Price": Price,
    }  # data is a dictionary
    with open("Items.csv", "a", newline="") as outfile:  # opens file in append mode
        writer = csv.DictWriter(outfile, fieldnames=data.keys())
        writer.writerow(data)  # writes data to file


def search_csv(Item):
    item_rows = []
    # search for item in Items.csv
    with open("Items.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == Item:
                item_rows.append(row)
    if len(item_rows) == 0:
        return None
    else:
        return item_rows


def sort_list(list):
    new_list = []
    for item in list:
        price = float(item[3])  # convert the price to a float
        weight = float(item[2])  # convert the weight to a float
        total_price = price / weight  # calculate the price per weight
        item = tuple(item) + (total_price,)  # add the price per weight to the tuple
        new_list.append(item)  # add the tuple to the list
    new_list.sort(key=lambda x: x[4])  # sort the list by the price per weight
    return new_list


def sort_list_budget(list, budget):
    budget = float(budget)  # convert to float
    within_budget = []
    outside_budget = []
    for item in list:
        if float(item[3]) > budget:  # if the cost is greater than the budget
            outside_budget.append(item)  # append to the outside budget list
        else:
            within_budget.append(item)  # append to the within budget list
    return within_budget, outside_budget  # return the two lists


budget = check_float("Enter the budget: $ ")

while True:
    product_name = Check_Blank("Enter the product name: ").lower()
    if product_name == "x":
        break
    if search_csv(product_name) is not None:
        csv_list = search_csv(product_name)
        console.print("\nProduct has been entered before\n", style="bold green")
        choice = ""
        while choice != "y" and choice != "n":
            choice = input("Would you like to autocomplete? (y/n): ").lower()
        if choice == "y":
            if len(csv_list) == 1:
                item_list.append(csv_list[0])
                continue
            else:
                loop = 0  # loop counter
                table = Table(
                    title="Autocomplete options"
                )  # create a table with the autocomplete options
                table.add_column("Option", style="cyan")
                table.add_column("Name")
                table.add_column("weight")
                table.add_column("Price")  # add columns to the table
                for item in csv_list:  # for each item in the list
                    # print(loop, item)
                    name = item[0]  # get the name
                    weight = str(item[2]) + " " + item[1]  # get the weight
                    price = "$" + str(item[3])  # get the price
                    table.add_row(
                        str(loop), name, weight, price
                    )  # add rows to the table
                    loop += 1  # increment the loop counter
                console.print(table)  # print the table
                choice = int(input("\nEnter the number of the item: "))
                item_list.append(csv_list[int(choice)])
                continue
    unit, amount = get_unit()
    price = check_price()
    append_list(product_name, unit, amount, price)
    item_list.append([product_name, unit, amount, price])

item_list = sort_list(item_list)
within, outside = sort_list_budget(item_list, budget)

# print each list as a table

table = Table(title="Within Budget")
table.add_column("Name")
table.add_column("Weight")
table.add_column("Price")
table.add_column("Price per Kg")

for item in within:
    table.add_row(str(item[0]), str(item[2]), str(item[3]), str(item[4]))
console.print(table)

table = Table(title="Outside Budget")
table.add_column("Name")
table.add_column("Weight")
table.add_column("Price")
table.add_column("Price per Kg")
for item in outside:
    table.add_row(str(item[0]), str(item[2]), str(item[3]), str(item[4]))
console.print(table)