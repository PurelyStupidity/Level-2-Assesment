from traceback import print_tb


budget = 8

list = [('banana', 'g', '3', '1.50', 0.5), ('Tuy', 'g', '2', '5', 2.5), ('coffee', 'g', '1', '3', 3.0), ('apple', 'g', '1', '9', 9)]

def sort_list_budget(list, budget):
    budget = float(budget)
    for item in list:
        cost = float(item[3])
        print(cost)

sort_list_budget(list, budget)