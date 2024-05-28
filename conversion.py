def convert_time(time_value, time_unit):
    try:

        if time_unit == "hours":
            minutes = time_value * 60
            seconds = time_value * 3600
            print(f"{time_value} hours is approximately {minutes:.2f} minutes or {seconds:.2f} seconds.")
            print('-\n')
        elif time_unit == "minutes":
            hours = time_value / 60
            seconds = time_value * 60
            print(f"{time_value} minutes is approximately {hours:.2f} hours or {seconds:.2f} seconds.")
            print('-\n')
        elif time_unit == "seconds":
            hours = time_value / 3600
            minutes = time_value / 60
            print(f"{time_value} seconds is approximately {hours:.2f} hours or {minutes:.2f} minutes.")
            print('-\n')
        else:
            print("Invalid time unit. Please enter 'hours', 'minutes', or 'seconds'.")

    except ValueError:
        print("Invalid input. Please enter a valid numeric value for time.")

def convert_distance(distance_value, distance_unit):
    try:
        if distance_unit == "m":
            km = distance_value / 1000
            cm = distance_value * 100
            print(f"{distance_value} meters is approximately {km:.2f} kilometers or {cm:.2f} centimeters.")
            print('-\n')
        elif distance_unit == "km":
            meters = distance_value * 1000
            cm = distance_value * 100000
            print(f"{distance_value} kilometers is approximately {meters:.2f} meters or {cm:.2f} centimeters.")
        elif distance_unit == "cm":
            meters = distance_value / 100
            km = distance_value / 100000
            print(f"{distance_value} centimeters is approximately {meters:.2f} meters or {km:.2f} kilometers.")
            print('\n')
        else:
            print("Invalid distance unit. Please enter 'm', 'km', or 'cm'.")

    except ValueError:
        print("Invalid input. Please enter a valid numeric value for distance.")

def convert_mass(mass_value, mass_unit):
    try:

        if mass_unit == "g":
            kg = mass_value / 1000
            tonnes = mass_value / 1000000
            print(f"{mass_value} grams is approximately {kg:.2f} kilograms or {tonnes:.2f} tonnes.")
            print('\n')
        elif mass_unit == "kg":
            grams = mass_value * 1000
            tonnes = mass_value / 1000
            print(f"{mass_value} kilograms is approximately {grams:.2f} grams or {tonnes:.2f} tonnes.")
            print('\n')
        elif mass_unit == "tonnes":
            grams = mass_value * 1000000
            kg = mass_value * 1000
            print(f"{mass_value} tonnes is approximately {grams:.2f} grams or {kg:.2f} kilograms.")
            print('\n')
        else:
            print("Invalid mass unit. Please enter 'g', 'kg', or 'tonnes'.")

    except ValueError:
        print("Invalid input. Please enter a valid numeric value for mass.")


while True:
    value = int(input("Enter the value: "))
    ask = input(str("Time, distance or mass? (t,d,m): "))

    if ask == "t":
        time_unit = input("Enter the time unit (hours/minutes/seconds): ").lower()
        convert_time(value, time_unit)

    elif ask == "d":
        distance_unit = input("Enter the distance unit (m/km/cm): ").lower()
        convert_distance(value, distance_unit)

    elif ask == "m":
        mass_unit = input("Enter the mass unit (g/kg/tonnes): ").lower()
        convert_mass(value, mass_unit)

        