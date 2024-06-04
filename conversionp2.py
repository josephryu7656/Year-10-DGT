# Author: Joseph Ryu
# Date: 
# Adding Time 2024/5/22
# Adding Distance and Mass function 2024/5/24
# Optimizing code 2024/6/5
#Distance conversion function
def distance_conversion(value, from_unit, to_unit):
    # Uses dictionary to define the value of each conversion
    conversion_factors = {
        "cm": {"m": 0.01, "mm": 10, "km": 0.000001},
        "m": {"cm": 100, "mm": 1000, "km": 0.001},
        "mm": {"cm": 0.1, "m": 0.001, "km": 1e-6},
        "km": {"cm": 100000, "m": 1000, "mm": 1e+6},
    }
    # The program will try to enter the value to be multipied with the conversion factors. If there is a error it will print "error" and restart the loop
    try:
        #Multiplies the entered value and it will detect the unit
        result = value * conversion_factors[from_unit][to_unit]
        print(f"{result:.2f}{to_unit}")
    except ValueError:
        print("errror")


#Very similar to the other function
def time_conversion(value, from_unit, to_unit):
    conversion_factors = {
        "seconds": {"minutes": 0.016667, "hours": 2.778e-4, "days": 1.1575e-5},
        "minutes": {"seconds": 60, "hours": 0.016667, "days":6.94e-4},
        "hours": {"seconds": 3600, "minutes": 60, "days": 0.041667},
        "days": {"seconds": 86400, "minutes": 1440, "hours": 24},
    }

    try:
        result = value * conversion_factors[from_unit][to_unit]
        print(f"{result:.2f}{to_unit}")
    except ValueError:
        print("error")


# Also similar to the other function
def mass_conversion(value, from_unit, to_unit):
    conversion_factors = {
        "mg": {"g": 0.01, "kg": 0.00001, "t": 0.00000001},
        "g": {"mg": 100, "kg": 0.001, "t":0.000001},
        "kg": {"mg": 100000, "g": 1000, "t": 0.001},
        "t": {"mg": 1e-9, "g": 1e-6, "kg": 1000},
    }

    try:
        result = value * conversion_factors[from_unit][to_unit]
        print(f"{result:.2f}{to_unit}")
    except ValueError:
        print("error")


# When program runs, loop
check = False
while not check:
    print("Unit Conversion Calculator")
    print("Which unit of measurement would you like to convert?")
    try:
        #Asks first for what unit the user will want to convert.
        ask = input(str("Time, Distance, Mass(t, d, m) >"))
        if ask == "t": 
            v = int(input("Enter the value > "))
            p = input(str("From (seconds, minutes, hours, days) > "))
            c = input(str("To (seconds, minutes, hours, days) > "))
            time_conversion(v, p, c)
            input(str("run again or exit? (r, e) > "))
            if input =="e":
                check = True
            else:
                pass
    
        elif ask == "d": 
            v = int(input("Enter the value > "))
            p = input(str("From (mm, cm, m, km) > "))
            c = input(str("To (mm, cm, m, km) > "))
            distance_conversion(v, p, c)
            input(str("run again or exit? (r, e) > "))
            if input =="e":
                check = True
            else:
                pass

        elif ask == "m": 
            v = int(input("Enter the value > "))
            p = input(str("From (mg, g, kg, t) > "))
            c = input(str("To (mg, g, kg, t) > "))
            #function has been asked for value, from unit and to unit.
            mass_conversion(v, p, c)
            #Option for user to restart program or exit program.
            input(str("run again or exit? (r, e) > "))
            if input =="e":
                check = True
            else:
                pass
                
        else:
            print("tbc")

    # Will print error and restart loop if a value error occurs
    except ValueError:
        print("Error")
    
    



