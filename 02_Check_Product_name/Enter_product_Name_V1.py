# ask user for Product name and if its empty then ask again.
def Check_Blank(question):
    while True:
        text = input(question)
        if text.isalpha() == True:
            return text
        else:
            print("Please enter a valid name.")


while True:
    print(Check_Blank("What is your product name? "))