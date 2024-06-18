# Author: Joseph Ryu
# Date: 2024/5/22
# Adding Time 2024/5/22
# Adding Distance and Mass function 2024/5/24
# Optimizing code 2024/6/5
# Adding comments 2024/6/7
# Further optimzation and rewrite of code 2024/06/17\

def num_check(question):
    error = "Please enter a valid input"
    while True:

        try:
            number = float(input(question))
            if number > 0:
                return number
            else:
                print(error)

        except ValueError:
            print(error)

def input_check(question, type):
    error = "Please enter a valid input"
    if type == "t":
        while True:
            try:
                unit = str(input(question))
                if unit in ["seconds", "minutes", "hours", 'days']:
                    return unit
                else:
                    print(error)
                    
            except ValueError:
                print(error)
    elif type == "d":
        while True:
            try:
                unit = str(input(question))
                if unit in ["cm", "m", "mm", "km"]:
                    return unit
                else:
                    print(error)
            except ValueError:
                print(error)

    elif type == "m":
        while True:
            try:
                unit = str(input(question))
                if unit in ["mg", "g", "kg", "t"]:
                    return unit
                else:
                    print(error)
            except ValueError:
                print(error)

    else:
        print("Invalid")

def distance_conversion(value, from_unit, to_unit):
    # The function parameters carry the data, which is called inside the while True loop
    # This list shows the conversion factors of each unit
    conversion_factors = {
        "cm": {"m": 0.01, "mm": 10, "km": 0.000001},
        "m": {"cm": 100, "mm": 1000, "km": 0.001},
        "mm": {"cm": 0.1, "m": 0.001, "km": 1e-6},
        "km": {"cm": 100000, "m": 1000, "mm": 1e+6},
    }
    try:
        result = value * conversion_factors[from_unit][to_unit]
        return f"{value} {from_unit} is {result:.2f} {to_unit}"
    except KeyError:
        return "Invalid unit conversion."

def time_conversion(value, from_unit, to_unit):
    # Each conversion function is very similar to each other, only difference being the dictionaries having different keys and values. 
    conversion_factors = {
        "seconds": {"minutes": 0.016667, "hours": 2.778e-4, "days": 1.1575e-5},
        "minutes": {"seconds": 60, "hours": 0.016667, "days": 6.94e-4},
        "hours": {"seconds": 3600, "minutes": 60, "days": 0.041667},
        "days": {"seconds": 86400, "minutes": 1440, "hours": 24},
    }
    try:
        result = value * conversion_factors[from_unit][to_unit]
        return f"{value} {from_unit} is {result:.2f} {to_unit}"
    except KeyError:
        return "Invalid unit conversion."

def mass_conversion(value, from_unit, to_unit):
    conversion_factors = {
        "mg": {"g": 0.01, "kg": 0.00001, "t": 0.00000001},
        "g": {"mg": 100, "kg": 0.001, "t": 0.000001},
        "kg": {"mg": 100000, "g": 1000, "t": 0.001},
        "t": {"mg": 1e+9, "g": 1e+6, "kg": 1000},
    }
    try:
        result = value * conversion_factors[from_unit][to_unit]
        return f"{value} {from_unit} is {result:.2f} {to_unit}"
    except KeyError:
        return "Invalid unit conversion."

def unit_conversion(value, from_unit, to_unit, conversion_type):
    # For more simplicity, a unit conversion function is made to handle errors and make code more flexible.
    if conversion_type == 'distance':
        return distance_conversion(value, from_unit, to_unit)
    elif conversion_type == 'time':
        return time_conversion(value, from_unit, to_unit)
    elif conversion_type == 'mass':
        return mass_conversion(value, from_unit, to_unit)
    else:
        return "Invalid conversion type."

# Main loop
def main():
    while True:
        print("Unit Conversion Calculator")
        conversion_type = input("Which unit of measurement would you like to convert? (t: Time, d: Distance, m: Mass) > ").lower()
        if conversion_type not in ['t', 'd', 'm']:
            print("Invalid choice. Please enter 't', 'd', or 'm'.")
            continue

        value = num_check("Enter the value > ")
        # if not value.isdigit():
        #     print("Invalid value. Please enter a numeric value.")
        #     continue

        if conversion_type == 't':
            from_unit = input_check("From (seconds, minutes, hours, days) > ", "t")
               
            to_unit = input_check("To (seconds, minutes, hours, days) > ", "t")
            result = unit_conversion(value, from_unit, to_unit, 'time')
        elif conversion_type == 'd':
            from_unit = input_check("From (mm, cm, m, km) > ", "d")
            to_unit = input_check("To (mm, cm, m, km) > ", "d")
            result = unit_conversion(value, from_unit, to_unit, 'distance')
            # Conversion function being called.
        elif conversion_type == 'm':
            from_unit = input_check("From (mg, g, kg, t) > ", "d")
            to_unit = input_check("To (mg, g, kg, t) > ", "d")
            result = unit_conversion(value, from_unit, to_unit, 'mass')

        print(result)
        
        again = input("Run again or exit? (r: run again, e: exit) > ").lower()
        if again == 'e':
            break



if __name__ == "__main__":
    main()
# This is used to make the main loop clearer for the computer and adds more modularity.