#ask user to enter unit, check if unit contains numbers, if it doesnt then ask again, if it does then continue, get the letters from unit e.g L or KG, if there is no unit then ask user to enter again. if the unit is ml or g then convert it to L or KG.

def check_unit(unit):
    unit = unit.upper()
    if unit == "L" or unit == "KG":
        return unit
    elif unit.isnumeric() == True:
        return unit
    else:
        return False