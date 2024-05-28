def distance_convertion(value, from_unit, to_unit):
    conversion_factors = {
        "cm": {"m": 0.01, "mm": 10},
        "m": {"cm": 100, "mm": 1000, "km": 0.001},
        "mm": {"cm": 0.1, "m": 0.001, "km": 1e-6},
        "km": {"cm": 100000, "m": 1000, "mm": 1e+6},
    }

    try:
        result = value * conversion_factors[from_unit][to_unit]
        print(f"{result}{to_unit}")
    except ValueError:
        print("errror")

def time_convertion(value, from_unit, to_unit):
    conversion_factors = {
        "seconds": {"minutes": 0.016667, "hours": 2.778e-4},
        "minutes": {"seconds": 60, "hours": 0.016667, "days":6.94e-4},
        "hours": {"seconds": 3600, "minutes": 60, "days": 0.041667},
        "days": {"seconds": 86400, "minutes": 1440, "hours": 24},
    }

    try:
        result = value * conversion_factors[from_unit][to_unit]
        print(f"{result:.2f}{to_unit}")
    except ValueError:
        print("errror")

def mass_conversion(value, from_unit, to_unit):
    conversion_factors = {
        "seconds": {"minutes": 0.016667, "hours": 2.778e-4},
        "minutes": {"seconds": 60, "hours": 0.016667, "days":6.94e-4},
        "hours": {"seconds": 3600, "minutes": 60, "days": 0.041667},
        "days": {"seconds": 86400, "minutes": 1440, "hours": 24},
    }

    try:
        result = value * conversion_factors[from_unit][to_unit]
        print(f"{result:.2f}{to_unit}")
    except ValueError:
        print("errror")

while True:
    ask = input(str("Time, Distance(t, d)"))
    if ask == "t": 
        v = int(input("Enter the value > "))
        p = input(str("From (seconds, minutes, hours, days) > "))
        c = input(str("To (seconds, minutes, hours, days) > "))
        time_convertion(v, p, c)
    
    elif ask == "d": 
        v = int(input("Enter the value > "))
        p = input(str("From (mm, cm, m, km) > "))
        c = input(str("To (mm, cm, m, km) > "))
        distance_convertion(v, p, c)
    else:
        print("tbc")
    
    