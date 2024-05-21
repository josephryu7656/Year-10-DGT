# def num_check(question):
#     keep_going = " "
#     while 


while True:
    print("---------")
    try:
        width = int(input("Width > "))
        length = int(input("Length > "))
        m_cost = int(input("Cost/m > "))

        if width > 0 and length > 0:
            perimeter = width + length
            perimeter += perimeter
            cost = perimeter*m_cost
            print(f"Perimeter: {perimeter} m")
            print(f"Cost: ${cost}")

            input("Again <enter> >")
            pass
        else:
            print("Please enter a valid value")
            break
    except ValueError:
        print("Error")

    