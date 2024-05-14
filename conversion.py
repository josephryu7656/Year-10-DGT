def convert_time():
    try:
        time_value = float(input("Enter the time value: "))
        time_unit = input("Enter the time unit (hours/minutes/seconds): ").lower()

        if time_unit == "hours":
            minutes = time_value * 60
            seconds = time_value * 3600
            print(f"{time_value} hours is approximately {minutes:.2f} minutes or {seconds:.2f} seconds.")
        elif time_unit == "minutes":
            hours = time_value / 60
            seconds = time_value * 60
            print(f"{time_value} minutes is approximately {hours:.2f} hours or {seconds:.2f} seconds.")
        elif time_unit == "seconds":
            hours = time_value / 3600
            minutes = time_value / 60
            print(f"{time_value} seconds is approximately {hours:.2f} hours or {minutes:.2f} minutes.")
        else:
            print("Invalid time unit. Please enter 'hours', 'minutes', or 'seconds'.")

    except ValueError:
        print("Invalid input. Please enter a valid numeric value for time.")

def convert_distance():
    try:
        distance_value = float(input("Enter the distance value: "))
        distance_unit = input("Enter the distance unit (m/km/cm): ").lower()

        if distance_unit == "m":
            km = distance_value / 1000
            cm = distance_value * 100
            print(f"{distance_value} meters is approximately {km:.2f} kilometers or {cm:.2f} centimeters.")
        elif distance_unit == "km":
            meters = distance_value * 1000
            cm = distance_value * 100000
            print(f"{distance_value} kilometers is approximately {meters:.2f} meters or {cm:.2f} centimeters.")
        elif distance_unit == "cm":
            meters = distance_value / 100
            km = distance_value / 100000
            print(f"{distance_value} centimeters is approximately {meters:.2f} meters or {km:.2f} kilometers.")
        else:
            print("Invalid distance unit. Please enter 'm', 'km', or 'cm'.")

    except ValueError:
        print("Invalid input. Please enter a valid numeric value for distance.")

def convert_mass():
    try:
        mass_value = float(input("Enter the mass value: "))
        mass_unit = input("Enter the mass unit (g/kg/tonnes): ").lower()

        if mass_unit == "g":
            kg = mass_value / 1000
            tonnes = mass_value / 1000000
            print(f"{mass_value} grams is approximately {kg:.2f} kilograms or {tonnes:.2f} tonnes.")
        elif mass_unit == "kg":
            grams = mass_value * 1000
            tonnes = mass_value / 1000
            print(f"{mass_value} kilograms is approximately {grams:.2f} grams or {tonnes:.2f} tonnes.")
        elif mass_unit == "tonnes":
            grams = mass_value * 1000000
            kg = mass_value * 1000
            print(f"{mass_value} tonnes is approximately {grams:.2f} grams or {kg:.2f} kilograms.")
        else:
            print("Invalid mass unit. Please enter 'g', 'kg', or 'tonnes'.")

    except ValueError:
        print("Invalid input. Please enter a valid numeric value for mass.")

if __name__ == "__main__":
    print("Welcome to the Unit Converter!")
    print("Choose an option:")
    print("1. Convert Time")
    print("2. Convert Distance")
    print("3. Convert Mass")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        convert_time()
    elif choice == "2":
        convert_distance()
    elif choice == "3":
        convert_mass()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")